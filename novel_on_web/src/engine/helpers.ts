import type {
  Beat,
  ChapterGenerator,
  EndingTone,
  EpitaphVariant,
  ImageBeat,
  PlayAgainPosition,
  PlayerState,
  Prompt,
} from "./types";

export function text(t: string): Beat {
  return { kind: "text", text: t.trim() };
}

export function art(t: string): Beat {
  return { kind: "art", text: t };
}

export function typewriter(t: string, cps = 60): Beat {
  return { kind: "typewriter", text: t.trim(), cps };
}

export function symbol(opts?: {
  symbol?: string;
  numLines?: number;
  sleepSeconds?: number;
}): Beat {
  return {
    kind: "symbol",
    symbol: opts?.symbol ?? "*",
    numLines: opts?.numLines ?? 7,
    sleepSeconds: opts?.sleepSeconds ?? 0.5,
  };
}

export function pause(seconds: number): Beat {
  return { kind: "pause", seconds };
}

export function section(level: number, title: string): Beat {
  return { kind: "section", level, title };
}

export function endingMode(opts: {
  titleSuffix: string;
  tone: EndingTone;
}): Beat {
  return { kind: "endingMode", titleSuffix: opts.titleSuffix, tone: opts.tone };
}

export function epitaph(opts: {
  text: string;
  variant?: EpitaphVariant;
  hold?: number;
}): Beat {
  return {
    kind: "epitaph",
    text: opts.text,
    variant: opts.variant,
    hold: opts.hold,
  };
}

export function credits(opts: { lines: string[]; hold?: number }): Beat {
  return { kind: "credits", lines: opts.lines, hold: opts.hold };
}

export function playAgain(opts?: { position?: PlayAgainPosition }): Beat {
  return { kind: "playAgain", position: opts?.position };
}

const IMAGE_BASE = `${import.meta.env.BASE_URL}images`;

export function imageBg(num: number | null): ImageBeat {
  return {
    kind: "image",
    layer: "background",
    src: num === null ? null : `${IMAGE_BASE}/back_${num}.jpg`,
  };
}

export function imageFg(num: number | null): ImageBeat {
  return {
    kind: "image",
    layer: "foreground",
    src: num === null ? null : `${IMAGE_BASE}/level_${num}.webp`,
  };
}

export function imageEnd(num: number | null): ImageBeat {
  return {
    kind: "image",
    layer: "end",
    src: num === null ? null : `${IMAGE_BASE}/end_${num}.webp`,
  };
}

export function ynPrompt(question: string, opts?: { noRecap?: boolean }): Prompt {
  return { kind: "yn", question, noRecap: opts?.noRecap };
}

export function multiPrompt(
  question: string,
  options: { key: string; label: string }[],
  opts?: { noRecap?: boolean },
): Prompt {
  return { kind: "multi", question, options, noRecap: opts?.noRecap };
}

export function freePrompt(question: string, opts?: { noRecap?: boolean }): Prompt {
  return { kind: "free", question, noRecap: opts?.noRecap };
}

export function expandIdea(state: PlayerState, expansion: string): PlayerState {
  const desc =
    state.ideaDescription.trim().toLowerCase() === "unknown"
      ? expansion
      : `${state.ideaDescription} and ${expansion}`;
  return { ...state, ideaDescription: desc };
}

export function addCamp(state: PlayerState, campName: string): PlayerState {
  if (state.visitedCamps.includes(campName)) return state;
  return { ...state, visitedCamps: [...state.visitedCamps, campName] };
}

export function addSector(state: PlayerState, sector: string): PlayerState {
  if (state.sectors.includes(sector)) return state;
  return { ...state, sectors: [...state.sectors, sector] };
}

export function* askYn(
  question: string,
  opts?: { noRecap?: boolean },
): Generator<Prompt, boolean, any> {
  const answer = (yield ynPrompt(question, opts)) as boolean;
  return answer;
}

export function* askMulti(
  question: string,
  options: { key: string; label: string }[],
  opts?: { noRecap?: boolean },
): Generator<Prompt, string, any> {
  const answer = (yield multiPrompt(question, options, opts)) as string;
  return answer;
}

export function* askFree(
  question: string,
  opts?: { noRecap?: boolean },
): Generator<Prompt, string, any> {
  const answer = (yield freePrompt(question, opts)) as string;
  return answer;
}

export function isPrompt(v: Beat | Prompt): v is Prompt {
  return v.kind === "yn" || v.kind === "multi" || v.kind === "free";
}

export function isImage(v: Beat | Prompt): v is ImageBeat {
  return v.kind === "image";
}

export type ChapterFactory = (
  state: PlayerState,
  handoff: Record<string, unknown>
) => ChapterGenerator;
