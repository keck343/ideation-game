import { useCallback, useEffect, useRef, useState } from "react";
import type {
  Answer,
  Beat,
  ChapterGenerator,
  ChapterId,
  EndingTone,
  PlayAgainPosition,
  PlayerState,
  Prompt,
  Transition,
} from "./types";
import { initialPlayerState } from "./types";
import { isImage, isPrompt, type ChapterFactory } from "./helpers";
import { writeSave, clearSave, type SaveGame } from "./saveState";

function formatRecap(p: Prompt, answer: Answer): string {
  if (p.kind === "yn") {
    return `${p.question} - ${answer ? "Yes" : "No"}`;
  }
  if (p.kind === "multi") {
    const opt = p.options.find((o) => o.key === answer);
    return `${p.question} - ${opt?.label ?? String(answer)}`;
  }
  return `${p.question} - ${String(answer)}`;
}

export type EndingMode = {
  titleSuffix: string;
  tone: EndingTone;
};

export type StoryState = {
  beats: Beat[];
  prompt: Prompt | null;
  background: string | null;
  foreground: string | null;
  endImage: string | null;
  player: PlayerState;
  chapterId: ChapterId;
  finished: boolean;
  endingMode: EndingMode | null;
  currentCard: Beat | null;
  currentCardVersion: number;
  showPlayAgain: boolean;
  playAgainPosition: PlayAgainPosition;
  restoredCount: number;
};

type Props = {
  chapters: Record<ChapterId, ChapterFactory>;
  initialChapter?: ChapterId;
  savedGame?: SaveGame;
};

// Must match the SceneView collapse animation so beats don't emit
// while the prompt is still fading out.
const PROMPT_COLLAPSE_MS = 380;

function beatDelayMs(b: Beat): number {
  switch (b.kind) {
    case "text":
      return Math.min(Math.max(b.text.length * 28, 900), 4200);
    case "art":
      return 900;
    case "typewriter":
      return (b.text.length / (b.cps ?? 60)) * 1000 + 500;
    case "symbol":
      return (b.numLines ?? 7) * (b.sleepSeconds ?? 0.5) * 1000 + 300;
    case "section":
      return 900;
    case "pause":
      return b.seconds * 1000;
    case "image":
      return 0;
    case "epitaph":
      return b.hold ?? Math.min(Math.max(b.text.length * 55, 2800), 7000);
    case "credits":
      return b.hold ?? 9000;
    case "endingMode":
    case "playAgain":
      return 0;
  }
}

export function useStory({
  chapters,
  initialChapter = "intro",
  savedGame,
}: Props) {
  const [beats, setBeats] = useState<Beat[]>([]);
  const [prompt, setPrompt] = useState<Prompt | null>(null);
  const [background, setBackground] = useState<string | null>(null);
  const [foreground, setForeground] = useState<string | null>(null);
  const [endImage, setEndImage] = useState<string | null>(null);
  const [player, setPlayer] = useState<PlayerState>(initialPlayerState("a"));
  const [chapterId, setChapterId] = useState<ChapterId>(initialChapter);
  const [finished, setFinished] = useState(false);
  const [endingMode, setEndingMode] = useState<EndingMode | null>(null);
  const [currentCard, setCurrentCard] = useState<Beat | null>(null);
  const [currentCardVersion, setCurrentCardVersion] = useState(0);
  const [showPlayAgain, setShowPlayAgain] = useState(false);
  const [playAgainPosition, setPlayAgainPosition] =
    useState<PlayAgainPosition>("top");
  const [restoredCount, setRestoredCount] = useState(0);

  const endingModeRef = useRef<EndingMode | null>(null);
  endingModeRef.current = endingMode;

  const genRef = useRef<ChapterGenerator | null>(null);
  const timerRef = useRef<number | null>(null);
  const skipRef = useRef<(() => void) | null>(null);
  const startedRef = useRef(false);

  // Save-state tracking refs
  const chapterIdRef = useRef<ChapterId>(initialChapter);
  const playerRef = useRef<PlayerState>(initialPlayerState("a"));
  const answersRef = useRef<Answer[]>([]);

  const cancelTimer = () => {
    if (timerRef.current !== null) {
      window.clearTimeout(timerRef.current);
      timerRef.current = null;
    }
    skipRef.current = null;
  };

  const persistSave = useCallback(() => {
    writeSave({
      version: __STORY_VERSION__,
      chapterId: chapterIdRef.current,
      playerState: playerRef.current,
      answers: [...answersRef.current],
      timestamp: Date.now(),
    });
  }, []);

  const handleTransition = useCallback(
    (t: Transition) => {
      playerRef.current = t.state;
      chapterIdRef.current = t.toChapter;

      setPlayer(t.state);
      setChapterId(t.toChapter);

      if (t.handoff?.done === true) {
        setFinished(true);
        genRef.current = null;
        clearSave();
        return;
      }
      const factory = chapters[t.toChapter];
      if (!factory) {
        setFinished(true);
        return;
      }

      persistSave();

      const gen = factory(t.state, t.handoff);
      genRef.current = gen;
      drive(gen);
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [chapters, persistSave],
  );

  type YieldedResult = IteratorYieldResult<Beat | Prompt>;

  const drive = useCallback(
    (gen: ChapterGenerator, firstAnswer?: Answer, preYielded?: YieldedResult) => {
      cancelTimer();

      const pump = (answer?: Answer, pre?: YieldedResult) => {
        // abort if a newer generator has taken over
        if (genRef.current !== gen) return;

        const result = pre ?? (answer !== undefined ? gen.next(answer) : gen.next());

        if (result.done) {
          setPrompt(null);
          handleTransition(result.value);
          return;
        }

        const v = result.value;

        if (isImage(v)) {
          if (v.layer === "background") setBackground(v.src);
          else if (v.layer === "foreground") setForeground(v.src);
          else setEndImage(v.src);
          pump();
          return;
        }

        if (isPrompt(v)) {
          setPrompt(v);
          return;
        }

        if (v.kind === "endingMode") {
          setEndingMode({ titleSuffix: v.titleSuffix, tone: v.tone });
          pump();
          return;
        }

        if (v.kind === "playAgain") {
          setPlayAgainPosition(v.position ?? "top");
          setShowPlayAgain(true);
          pump();
          return;
        }

        const inEndingMode = endingModeRef.current !== null;

        if (v.kind === "pause") {
        } else if (inEndingMode) {
          setCurrentCard(v);
          setCurrentCardVersion((n) => n + 1);
        } else {
          setBeats((b) => [...b, v]);
        }

        const delay = beatDelayMs(v);
        const advance = () => {
          timerRef.current = null;
          skipRef.current = null;
          pump();
        };
        if (delay <= 0) {
          advance();
          return;
        }
        skipRef.current = () => {
          if (timerRef.current !== null) {
            window.clearTimeout(timerRef.current);
            advance();
          }
        };
        timerRef.current = window.setTimeout(advance, delay);
      };

      pump(firstAnswer, preYielded);
    },
    [handleTransition],
  );

  const restoreFromSave = useCallback(
    (save: SaveGame) => {
      answersRef.current = [...save.answers];

      const collectedBeats: Beat[] = [];
      let bg: string | null = null;
      let fg: string | null = null;
      let end: string | null = null;
      let eMode: EndingMode | null = null;
      let pAgain = false;
      let pAgainPos: PlayAgainPosition = "top";
      let lastEndingCard: Beat | null = null;
      let pendingPrompt: Prompt | null = null;

      let curState = initialPlayerState("a");
      let curHandoff: Record<string, unknown> = {};
      let curChapter: ChapterId = initialChapter;
      let targetGen: ChapterGenerator | null = null;
      let answerIdx = 0;
      let firstLiveResult: YieldedResult | undefined;

      outer: while (true) {
        const factory = chapters[curChapter];
        if (!factory) break;

        const gen = factory(curState, curHandoff);
        targetGen = gen;

        let pendingAnswer: Answer | undefined;

        while (true) {
          const result =
            pendingAnswer !== undefined ? gen.next(pendingAnswer) : gen.next();
          pendingAnswer = undefined;

          if (result.done) {
            const t = result.value;
            curState = t.state;
            curHandoff = t.handoff;
            curChapter = t.toChapter;
            if (t.handoff?.done === true) break outer;
            break;
          }

          const v = result.value;

          if (isImage(v)) {
            if (v.layer === "background") bg = v.src;
            else if (v.layer === "foreground") fg = v.src;
            else end = v.src;
            continue;
          }

          if (isPrompt(v)) {
            if (answerIdx < save.answers.length) {
              pendingAnswer = save.answers[answerIdx++];
              if (!v.noRecap) {
                collectedBeats.push({
                  kind: "text",
                  text: formatRecap(v, pendingAnswer),
                  italic: true,
                });
              }
              continue;
            }
            pendingPrompt = v;
            break outer;
          }

          if (v.kind === "endingMode") {
            eMode = { titleSuffix: v.titleSuffix, tone: v.tone };
            continue;
          }

          if (v.kind === "playAgain") {
            pAgain = true;
            pAgainPos = v.position ?? "top";
            continue;
          }

          // All answers consumed and we've reached the target chapter —
          // don't collect this beat; hand it to drive as the first live beat.
          if (
            answerIdx >= save.answers.length &&
            curChapter === save.chapterId &&
            v.kind !== "pause"
          ) {
            firstLiveResult = { done: false, value: v } as YieldedResult;
            break outer;
          }

          // Content beat — collect it
          if (v.kind !== "pause") {
            if (eMode) {
              lastEndingCard = v;
            } else {
              collectedBeats.push(v);
            }
          }
        }
      }

      // Apply all accumulated state
      genRef.current = targetGen;
      chapterIdRef.current = curChapter;
      playerRef.current = curState;

      setBeats(collectedBeats);
      setRestoredCount(collectedBeats.length);
      setBackground(bg);
      setForeground(fg);
      setEndImage(end);
      setPlayer(curState);
      setChapterId(curChapter);

      if (eMode) {
        setEndingMode(eMode);
        endingModeRef.current = eMode;
      }
      if (lastEndingCard) {
        setCurrentCard(lastEndingCard);
        setCurrentCardVersion(1);
      }
      if (pAgain) {
        setShowPlayAgain(true);
        setPlayAgainPosition(pAgainPos);
      }

      if (pendingPrompt) {
        setPrompt(pendingPrompt);
      } else if (targetGen) {
        const gen = targetGen;
        const pre = firstLiveResult;
        timerRef.current = window.setTimeout(() => {
          timerRef.current = null;
          drive(gen, undefined, pre);
        }, 750);
      }
    },
    [chapters, initialChapter, drive],
  );

  useEffect(() => {
    if (startedRef.current) return;
    startedRef.current = true;
    if (savedGame) {
      restoreFromSave(savedGame);
    } else {
      const factory = chapters[initialChapter];
      const gen = factory(initialPlayerState("a"), {});
      genRef.current = gen;
      chapterIdRef.current = initialChapter;
      playerRef.current = initialPlayerState("a");
      drive(gen);
    }
  }, [chapters, initialChapter, drive, savedGame, restoreFromSave]);

  const answer = useCallback(
    (a: Answer) => {
      const gen = genRef.current;
      if (!gen) return;
      answersRef.current.push(a);
      persistSave();
      setPrompt(null);
      cancelTimer();
      timerRef.current = window.setTimeout(() => {
        timerRef.current = null;
        drive(gen, a);
      }, PROMPT_COLLAPSE_MS);
    },
    [drive, persistSave],
  );

  const skip = useCallback(() => {
    skipRef.current?.();
  }, []);

  const reset = useCallback(() => {
    cancelTimer();
    clearSave();
    answersRef.current = [];
    chapterIdRef.current = initialChapter;
    playerRef.current = initialPlayerState("a");
    setBeats([]);
    setPrompt(null);
    setBackground(null);
    setForeground(null);
    setEndImage(null);
    setFinished(false);
    setEndingMode(null);
    endingModeRef.current = null;
    setCurrentCard(null);
    setCurrentCardVersion(0);
    setShowPlayAgain(false);
    setPlayAgainPosition("top");
    setRestoredCount(0);
    setChapterId(initialChapter);
    const factory = chapters[initialChapter];
    const gen = factory(initialPlayerState("a"), {});
    genRef.current = gen;
    drive(gen);
  }, [chapters, drive, initialChapter]);

  // debug helper: jump straight into any chapter with seeded state/handoff.
  // seedBeats lets you pre-populate the log (e.g. the level-0 title section).
  const jumpTo = useCallback(
    (
      target: ChapterId,
      playerPatch: Partial<PlayerState>,
      handoff: Record<string, unknown>,
      seedBeats: Beat[] = [],
    ) => {
      cancelTimer();
      answersRef.current = [];
      setBeats(seedBeats);
      setPrompt(null);
      setBackground(null);
      setForeground(null);
      setEndImage(null);
      setFinished(false);
      setEndingMode(null);
      endingModeRef.current = null;
      setCurrentCard(null);
      setCurrentCardVersion(0);
      setShowPlayAgain(false);
      setPlayAgainPosition("top");
      setRestoredCount(0);
      const nextPlayer: PlayerState = {
        ...initialPlayerState("a"),
        ...playerPatch,
      };
      playerRef.current = nextPlayer;
      chapterIdRef.current = target;
      setPlayer(nextPlayer);
      setChapterId(target);
      const factory = chapters[target];
      const gen = factory(nextPlayer, handoff);
      genRef.current = gen;
      drive(gen);
    },
    [chapters, drive],
  );

  return {
    state: {
      beats,
      prompt,
      background,
      foreground,
      endImage,
      player,
      chapterId,
      finished,
      endingMode,
      currentCard,
      currentCardVersion,
      showPlayAgain,
      playAgainPosition,
      restoredCount,
    } satisfies StoryState,
    answer,
    skip,
    reset,
    jumpTo,
  };
}
