export type Quote = { author: string; quote: string };

export const quotes: Record<string, Quote> = {
  a: {
    author: "William S. Burroughs",
    quote:
      "Cut ups are for everyone. Anybody can make cut ups. All Writing is cut-ups.",
  },
  b: {
    author: "Jose Ortega",
    quote:
      "I am I and my circumstance; and, if I do not save it, I do not save myself.",
  },
  c: {
    author: "Anne Bogart",
    quote:
      "We create truths by describing, or by re-describing, our beliefs and observations. Our task, and the task of every artist and scientist, is to re-describe our inherited assumptions and invented fictions in order to create new paradigms for the future",
  },
  d: {
    author: "Rosemarie Garland-Thompson",
    quote:
      "The task of a misfit is not to try and fail endlessly to somehow fit, but to develop alternative methods.",
  },
  e: {
    author: "the Shoe of Shoes, created by Julio Torres",
    quote: "I am difficult to explain and hard to draw. I am alive.",
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
