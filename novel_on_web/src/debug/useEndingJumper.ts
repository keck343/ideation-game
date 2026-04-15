import { useEffect } from "react";
import type { Beat, ChapterId, PlayerState } from "../engine/types";

// Debug: press 5, 6, 7, 8, or 9 to jump to a different ending sequence
// delete this file and its import in App.tsx to remove

type JumpFn = (
  target: ChapterId,
  playerPatch: Partial<PlayerState>,
  handoff: Record<string, unknown>,
  seedBeats?: Beat[],
) => void;

const titleSeed: Beat[] = [
  { kind: "section", level: 0, title: "Disambiguation" },
];

type Preset = {
  label: string;
  playerPatch: Partial<PlayerState>;
  handoff: Record<string, unknown>;
};

const presets: Record<string, Preset> = {
  5: {
    label: "novelist",
    playerPatch: { desiredEndStateKey: "a" },
    handoff: { finalCampName: "Konspiro", finalNumRoundsInCamp: 0 },
  },
  6: {
    label: "loss",
    playerPatch: { desiredEndStateKey: "b" },
    handoff: { finalCampName: "Konspiro", finalNumRoundsInCamp: 0 },
  },
  7: {
    label: "survival / relief",
    playerPatch: { desiredEndStateKey: "d" },
    handoff: { finalCampName: "Skalismo", finalNumRoundsInCamp: 2 },
  },
  8: {
    label: "survival / new camp",
    playerPatch: { desiredEndStateKey: "b" },
    handoff: { finalCampName: "Skalismo", finalNumRoundsInCamp: 2 },
  },
  9: {
    label: "survival / ego",
    playerPatch: { desiredEndStateKey: "e" },
    handoff: { finalCampName: "Skalismo", finalNumRoundsInCamp: 2 },
  },
};

export function useEndingJumper(jumpTo: JumpFn): void {
  useEffect(() => {
    console.info(
      "[debug] ending jumper — %s",
      Object.entries(presets)
        .map(([k, p]) => `${k.toUpperCase()}=${p.label}`)
        .join("  "),
    );
    const onKey = (e: KeyboardEvent) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      const target = e.target as HTMLElement | null;
      if (
        target &&
        (target.tagName === "TEXTAREA" ||
          target.tagName === "INPUT" ||
          target.isContentEditable)
      ) {
        return;
      }
      const preset = presets[e.key.toLowerCase()];
      if (!preset) return;
      e.preventDefault();
      console.info("[debug] jump →", preset.label);
      jumpTo("ending", preset.playerPatch, preset.handoff, titleSeed);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [jumpTo]);
}
