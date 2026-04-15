export type TextBeat = { kind: "text"; text: string };
export type ArtBeat = { kind: "art"; text: string };
export type TypewriterBeat = { kind: "typewriter"; text: string; cps?: number };
export type GrowingSymbolBeat = {
  kind: "symbol";
  symbol?: string;
  numLines?: number;
  sleepSeconds?: number;
};
export type ImageBeat = {
  kind: "image";
  layer: "background" | "foreground" | "end";
  src: string | null;
};
export type PauseBeat = { kind: "pause"; seconds: number };
export type SectionBeat = { kind: "section"; level: number; title: string };

export type EndingTone = "cold" | "neutral" | "warm";
export type EndingModeBeat = {
  kind: "endingMode";
  titleSuffix: string;
  tone: EndingTone;
};

export type EpitaphVariant = "default" | "large" | "footnote";
export type EpitaphBeat = {
  kind: "epitaph";
  text: string;
  variant?: EpitaphVariant;
  hold?: number;
};

export type CreditsBeat = {
  kind: "credits";
  lines: string[];
  hold?: number;
};

export type PlayAgainPosition = "top" | "bottom";
export type PlayAgainBeat = { kind: "playAgain"; position?: PlayAgainPosition };

export type Beat =
  | TextBeat
  | ArtBeat
  | TypewriterBeat
  | GrowingSymbolBeat
  | ImageBeat
  | PauseBeat
  | SectionBeat
  | EndingModeBeat
  | EpitaphBeat
  | CreditsBeat
  | PlayAgainBeat;

export type YesNoPrompt = { kind: "yn"; question: string };
export type MultiChoicePrompt = {
  kind: "multi";
  question: string;
  options: { key: string; label: string }[];
};
export type FreeTextPrompt = { kind: "free"; question: string };

export type Prompt = YesNoPrompt | MultiChoicePrompt | FreeTextPrompt;

export type Answer = boolean | string;

export type PlayerState = {
  playerQuoteKey: string;
  ideaDescription: string;
  visitedCamps: string[];
  rejectedCamps: string[];
  sectors: string[];
  rejectedSectors: string[];
  desiredEndStateKey: string;
  fame: boolean;
  noTokens: boolean;
};

export const initialPlayerState = (quoteKey: string): PlayerState => ({
  playerQuoteKey: quoteKey,
  ideaDescription: "unknown",
  visitedCamps: [],
  rejectedCamps: [],
  sectors: [],
  rejectedSectors: [],
  desiredEndStateKey: "a",
  fame: false,
  noTokens: false,
});

export type ChapterId =
  | "intro"
  | "chapter01"
  | "chapter02"
  | "chapter03"
  | "chapter04"
  | "chapter05"
  | "chapter06"
  | "ending";

export type Transition = {
  toChapter: ChapterId;
  state: PlayerState;
  handoff: Record<string, unknown>;
};

export type ChapterStep = IteratorResult<Beat | Prompt, Transition>;

export type ChapterGenerator = Generator<Beat | Prompt, Transition, Answer>;
