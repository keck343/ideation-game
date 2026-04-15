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
};

type Props = {
  chapters: Record<ChapterId, ChapterFactory>;
  initialChapter?: ChapterId;
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

export function useStory({ chapters, initialChapter = "intro" }: Props) {
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

  const endingModeRef = useRef<EndingMode | null>(null);
  endingModeRef.current = endingMode;

  const genRef = useRef<ChapterGenerator | null>(null);
  const timerRef = useRef<number | null>(null);
  const skipRef = useRef<(() => void) | null>(null);
  const startedRef = useRef(false);

  const cancelTimer = () => {
    if (timerRef.current !== null) {
      window.clearTimeout(timerRef.current);
      timerRef.current = null;
    }
    skipRef.current = null;
  };

  const handleTransition = useCallback(
    (t: Transition) => {
      setPlayer(t.state);
      setChapterId(t.toChapter);
      if (t.handoff?.done === true) {
        setFinished(true);
        genRef.current = null;
        return;
      }
      const factory = chapters[t.toChapter];
      if (!factory) {
        setFinished(true);
        return;
      }
      const gen = factory(t.state, t.handoff);
      genRef.current = gen;
      drive(gen);
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [chapters],
  );

  const drive = useCallback(
    (gen: ChapterGenerator, firstAnswer?: Answer) => {
      cancelTimer();

      const pump = (answer?: Answer) => {
        // abort if a newer generator has taken over
        if (genRef.current !== gen) return;

        const result = answer !== undefined ? gen.next(answer) : gen.next();

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

      pump(firstAnswer);
    },
    [handleTransition],
  );

  useEffect(() => {
    if (startedRef.current) return;
    startedRef.current = true;
    const factory = chapters[initialChapter];
    const gen = factory(initialPlayerState("a"), {});
    genRef.current = gen;
    drive(gen);
  }, [chapters, initialChapter, drive]);

  const answer = useCallback(
    (a: Answer) => {
      const gen = genRef.current;
      if (!gen) return;
      setPrompt(null);
      cancelTimer();
      timerRef.current = window.setTimeout(() => {
        timerRef.current = null;
        drive(gen, a);
      }, PROMPT_COLLAPSE_MS);
    },
    [drive],
  );

  const skip = useCallback(() => {
    skipRef.current?.();
  }, []);

  const reset = useCallback(() => {
    cancelTimer();
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
      const nextPlayer: PlayerState = {
        ...initialPlayerState("a"),
        ...playerPatch,
      };
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
    } satisfies StoryState,
    answer,
    skip,
    reset,
    jumpTo,
  };
}
