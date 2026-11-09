export type Quote = { author: string; quote: string };

export const quotes: Record<string, Quote> = {
  a: {
    author: "José Ortega y Gasset",
    quote:
      "I am I and my circumstance; and, if I do not save it, I do not save myself.",
  },
  b: {
    author: "Anne Bogart",
    quote:
      "We create truths by describing, or by re-describing, our beliefs and observations. Our task, and the task of every artist and scientist, is to re-describe our inherited assumptions and invented fictions in order to create new paradigms for the future",
  },
  c: {
    author: "Rosemarie Garland-Thompson",
    quote:
      "The task of a misfit is not to try and fail endlessly to somehow fit, but to develop alternative methods.",
  },
  d: {
    author: "the Shoe of Shoes, created by Julio Torres",
    quote: "I am difficult to explain and hard to draw. I am alive.",
  },
  e: {
    author: "Banksy",
    quote:
      "The greatest crimes in the world are not committed by people breaking the rules but by people following the rules. It's people who follow orders that drop bombs and massacre villages.",
  },
};

export const newIdea01 = "(๑'ᵕ'๑)⸝*";
export const newIdea02 = "₍^ >⩊< ^₎Ⳋ";
export const newIdea03 = "( ദ്ദി ˙ᗜ˙ )";
export const newIdea04 = "｡°(°¯᷄◠¯᷅°)°｡";

export const endStateMappings: Record<string, string> = {
  a: "you read a novel, all other outcomes are irrelevant",
  b: "your camp becomes the dominant voice in your sector",
  c: "your camp survives",
  d: "all camps survive & if beings exist they survive",
  e: "you achieve fame, all other outcomes are irrelevant",
  f: "you achieve fame & your camp survives - why do these need to be contradictory?",
};

export const MAX_ROUND = 10;
