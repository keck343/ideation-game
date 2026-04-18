import { useEffect, useState } from "react";
import { useStory } from "./engine/useStory";
import type { ChapterId } from "./engine/types";
import type { ChapterFactory } from "./engine/helpers";
import { preloadImages } from "./engine/preloadImages";
import { SceneView } from "./ui/SceneView";
import { ErrorBoundary } from "./ui/ErrorBoundary";
import { ResumePrompt } from "./ui/ResumePrompt";
import { readSave, clearSave, type SaveGame } from "./engine/saveState";
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
  const [save] = useState(() => readSave());
  const [choice, setChoice] = useState<"continue" | "new" | null>(
    save ? null : "new",
  );

  useEffect(() => {
    preloadImages();
  }, []);

  if (choice === null) {
    return (
      <ErrorBoundary>
        <ResumePrompt
          onContinue={() => setChoice("continue")}
          onNewGame={() => {
            clearSave();
            setChoice("new");
          }}
        />
      </ErrorBoundary>
    );
  }

  return (
    <ErrorBoundary>
      <Game savedGame={choice === "continue" ? save : undefined} />
    </ErrorBoundary>
  );
}

function Game({ savedGame }: { savedGame?: SaveGame | null }) {
  const { state, answer, skip, reset, jumpTo } = useStory({
    chapters,
    savedGame: savedGame ?? undefined,
  });
  useEndingJumper(jumpTo);

  return (
    <SceneView
      state={state}
      onAnswer={answer}
      onSkip={skip}
      onReset={reset}
    />
  );
}
