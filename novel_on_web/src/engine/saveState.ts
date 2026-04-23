import type { Answer, ChapterId, PlayerState } from "./types";

export type SaveGame = {
  version: string;
  chapterId: ChapterId;
  playerState: PlayerState;
  answers: Answer[];
  timestamp: number;
};

const KEY = "disambiguation-save";

export function writeSave(game: SaveGame): void {
  try {
    localStorage.setItem(KEY, JSON.stringify(game));
  } catch {}
}

export function readSave(): SaveGame | null {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as SaveGame;
    if (parsed.version !== __STORY_VERSION__) {
      clearSave();
      return null;
    }
    return parsed;
  } catch {
    return null;
  }
}

export function clearSave(): void {
  try {
    localStorage.removeItem(KEY);
  } catch {}
}
