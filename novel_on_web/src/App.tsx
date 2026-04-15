import { useEffect } from "react";
import { useStory } from "./engine/useStory";
import type { ChapterId } from "./engine/types";
import type { ChapterFactory } from "./engine/helpers";
import { preloadImages } from "./engine/preloadImages";
import { SceneView } from "./ui/SceneView";
import { ErrorBoundary } from "./ui/ErrorBoundary";
import { intro } from "./chapters/intro";
import { chapter01 } from "./chapters/chapter01";
import { chapter02 } from "./chapters/chapter02";
import { chapter03 } from "./chapters/chapter03";
import { chapter04 } from "./chapters/chapter04";
import { chapter05 } from "./chapters/chapter05";
import { chapter06 } from "./chapters/chapter06";
import { ending } from "./chapters/ending";
import { useEndingJumper } from "./debug/useEndingJumper";

const chapters: Record<ChapterId, ChapterFactory> = {
  intro,
  chapter01,
  chapter02,
  chapter03,
  chapter04,
  chapter05,
  chapter06,
  ending,
};

export default function App() {
  const { state, answer, skip, reset, jumpTo } = useStory({ chapters });
  useEndingJumper(jumpTo);
  useEffect(() => {
    preloadImages();
  }, []);
  return (
    <ErrorBoundary>
      <SceneView
        state={state}
        onAnswer={answer}
        onSkip={skip}
        onReset={reset}
      />
    </ErrorBoundary>
  );
}
