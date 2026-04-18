import {
  useCallback,
  useEffect,
  useRef,
  useState,
  type CSSProperties,
} from "react";
import type { StoryState } from "../engine/useStory";
import type { Answer, Beat, Prompt } from "../engine/types";
import { BeatDisplay } from "./BeatDisplay";
import { Choices } from "./Choices";
import { EndingOverlay } from "./EndingOverlay";
import { SkipContext } from "./SkipContext";

type Props = {
  state: StoryState;
  onAnswer: (a: Answer) => void;
  onSkip: () => void;
  onReset: () => void;
};

const COLLAPSE_MS = 380;
const CROSSFADE_MS = 1000;

type CrossfadeLayerProps = {
  src: string | null;
  className: string;
  style?: CSSProperties;
  visibleOpacity: number;
};

function CrossfadeLayer({
  src,
  className,
  style,
  visibleOpacity,
}: CrossfadeLayerProps) {
  const [srcs, setSrcs] = useState<[string | null, string | null]>([
    null,
    null,
  ]);
  const [active, setActive] = useState<0 | 1>(0);

  useEffect(() => {
    const cur = srcs[active];
    if (cur === src) return;
    const next = (1 - active) as 0 | 1;
    setSrcs((prev) => {
      const copy = [...prev] as [string | null, string | null];
      copy[next] = src;
      return copy;
    });
    setActive(next);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [src]);

  return (
    <>
      {[0, 1].map((i) => {
        const layerSrc = srcs[i];
        return (
          <div
            key={i}
            className={className}
            style={{
              ...style,
              backgroundImage: layerSrc ? `url(${layerSrc})` : undefined,
              opacity: i === active && layerSrc ? visibleOpacity : 0,
              transition: `opacity ${CROSSFADE_MS}ms ease`,
            }}
          />
        );
      })}
    </>
  );
}

export function SceneView({ state, onAnswer, onSkip, onReset }: Props) {
  const scrollRef = useRef<HTMLDivElement>(null);
  const prevBeats = useRef(state.beats.length);

  const [displayedPrompt, setDisplayedPrompt] = useState<Prompt | null>(
    state.prompt,
  );
  const [collapsing, setCollapsing] = useState(false);
  const [skipTick, setSkipTick] = useState(0);
  const [blackout, setBlackout] = useState(false);
  const resettingRef = useRef(false);

  const handleReset = useCallback(() => {
    if (resettingRef.current) return;
    resettingRef.current = true;
    setBlackout(true);
    window.setTimeout(() => {
      onReset();
    }, 550);
    window.setTimeout(() => {
      setBlackout(false);
      resettingRef.current = false;
    }, 1100);
  }, [onReset]);

  const handleSkip = useCallback(() => {
    setSkipTick((t) => t + 1);
    onSkip();
  }, [onSkip]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement | null;
      const isTyping =
        target &&
        (target.tagName === "TEXTAREA" ||
          target.tagName === "INPUT" ||
          target.isContentEditable);

      if (state.finished) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          handleReset();
        }
        return;
      }

      const prompt = state.prompt;
      if (prompt) {
        if (prompt.kind === "free") return; // let user type freely
        if (isTyping) return;
        if (prompt.kind === "yn") {
          if (e.key === "y" || e.key === "Y" || e.key === "1") {
            e.preventDefault();
            onAnswer(true);
          } else if (e.key === "n" || e.key === "N" || e.key === "2") {
            e.preventDefault();
            onAnswer(false);
          }
          return;
        }
        if (prompt.kind === "multi") {
          const match = prompt.options.find(
            (o) => o.key.toLowerCase() === e.key.toLowerCase(),
          );
          if (match) {
            e.preventDefault();
            onAnswer(match.key);
          }
          return;
        }
        return;
      }

      if (isTyping) return;
      if (e.key === " " || e.key === "Enter") {
        if (!canSkipRef.current) return;
        e.preventDefault();
        setSkipTick((t) => t + 1);
        onSkip();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [state.prompt, state.finished, onAnswer, onSkip, onReset]);

  useEffect(() => {
    if (state.prompt) {
      setDisplayedPrompt(state.prompt);
      setCollapsing(false);
      return;
    }
    if (displayedPrompt) {
      setCollapsing(true);
      const t = window.setTimeout(() => {
        setDisplayedPrompt(null);
        setCollapsing(false);
      }, COLLAPSE_MS);
      return () => window.clearTimeout(t);
    }
    return;
  }, [state.prompt, displayedPrompt]);

  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;
    if (state.beats.length > prevBeats.current) {
      el.scrollTo({ top: el.scrollHeight, behavior: "smooth" });
    }
    prevBeats.current = state.beats.length;
  }, [state.beats.length]);

  // pin scroll to bottom as prompt grows during animations
  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;
    const beatsEl = el.querySelector<HTMLElement>(".beats");
    if (!beatsEl) return;
    const ro = new ResizeObserver(() => {
      if (state.prompt || displayedPrompt) return;
      const dist = el.scrollHeight - (el.scrollTop + el.clientHeight);
      if (dist < 140) {
        el.scrollTop = el.scrollHeight;
      }
    });
    ro.observe(beatsEl);
    return () => ro.disconnect();
  }, [state.prompt, displayedPrompt]);

  // keeps the prompt comfortably positioned as screen size changes
  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;
    if (!displayedPrompt || collapsing) return;
    const raf = requestAnimationFrame(() => {
      const pEl = el.querySelector<HTMLElement>(".prompt-wrap");
      if (!pEl) return;
      const cRect = el.getBoundingClientRect();
      const pRect = pEl.getBoundingClientRect();
      const titleSafe = 0.16 * cRect.height;
      const bottomSafe = 0.14 * cRect.height;
      const available = cRect.height - titleSafe - bottomSafe;
      let delta: number;
      if (pRect.height <= available) {
        delta = pRect.bottom - (cRect.bottom - bottomSafe);
      } else {
        delta = pRect.top - (cRect.top + titleSafe);
      }
      if (Math.abs(delta) > 2) {
        el.scrollBy({ top: delta, behavior: "smooth" });
      }
    });
    return () => cancelAnimationFrame(raf);
  }, [displayedPrompt, collapsing]);

  const inEndingMode = state.endingMode !== null;
  const canSkip =
    !state.prompt && !displayedPrompt && !state.finished && !inEndingMode;
  const canSkipRef = useRef(canSkip);
  canSkipRef.current = canSkip;

  const titleBeat = state.beats.find(
    (b): b is Extract<Beat, { kind: "section" }> =>
      b.kind === "section" && b.level === 0,
  );
  const bodyBeats = titleBeat
    ? state.beats.filter((b) => b !== titleBeat)
    : state.beats;
  const bodyRestoredCount = titleBeat
    ? state.restoredCount - 1
    : state.restoredCount;

  return (
    <div className="scene-view">
      <CrossfadeLayer
        className="layer background"
        src={state.background}
        visibleOpacity={0.55}
      />
      <CrossfadeLayer
        className="layer foreground"
        src={state.foreground}
        visibleOpacity={0.35}
      />
      <div className={`end-backdrop${state.endImage ? " visible" : ""}`} />
      <CrossfadeLayer
        className="layer end-overlay"
        src={state.endImage}
        visibleOpacity={0.9}
      />

      <div
        className={`terminal-column${titleBeat ? " has-title" : ""}${
          inEndingMode ? " ending" : ""
        }`}
      >
        <div
          className={`terminal${canSkip ? " skippable" : ""}`}
          ref={scrollRef}
          onClick={canSkip ? handleSkip : undefined}
        >
          <div className="beats" aria-live="polite" aria-relevant="additions">
            <SkipContext.Provider value={skipTick}>
              {bodyBeats.map((b, i) => (
                <BeatDisplay
                  beat={b}
                  key={i}
                  restored={i < bodyRestoredCount}
                />
              ))}
            </SkipContext.Provider>
            {displayedPrompt && (
              <div
                key={displayedPrompt.question}
                className={`prompt-wrap${collapsing ? " collapsing" : ""}`}
                onClick={(e) => e.stopPropagation()}
              >
                <Choices
                  prompt={displayedPrompt}
                  onAnswer={onAnswer}
                  disabled={collapsing}
                />
              </div>
            )}
            {state.finished && !inEndingMode && (
              <div className="finished" onClick={(e) => e.stopPropagation()}>
                <button onClick={handleReset}>Play again</button>
              </div>
            )}
          </div>
        </div>
        <div className="fade-top" />
        {titleBeat && (
          <h2 className="title-bar">
            {titleBeat.title}
            {state.endingMode && (
              <span className="title-suffix">
                {state.endingMode.titleSuffix}
              </span>
            )}
          </h2>
        )}
      </div>

      <EndingOverlay
        mode={state.endingMode}
        card={state.currentCard}
        cardVersion={state.currentCardVersion}
        showPlayAgain={state.showPlayAgain}
        playAgainPosition={state.playAgainPosition}
        onReset={handleReset}
      />

      <div className={`blackout${blackout ? " on" : ""}`} />
    </div>
  );
}
