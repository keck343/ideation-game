import type { Camp } from "./camps";

export type Sector = {
  name: "Beit" | "Gimel";
  coreBelief: string;
  beingsExist: boolean;
  dinnerTalkingPoints: {
    sector: string;
    beings: string;
    disappearance: string;
    beingsCounterPoint: string;
    campInvitation: string;
  };
  brochureTagline: string;
  camps: Camp[];
};

export const beitSector: Sector = {
  name: "Beit",
  coreBelief: "There are no beings. Only optimizing the here and now.",
  beingsExist: false,
  dinnerTalkingPoints: {
    sector: "Beings do not exist.",
    beings: `"Fools claim that Beings exist in a physical realm connected to ours. Some even claim that we come out of their thoughts, as if we are not enough in and of ourselves. As if something as foolish as attention could control our fate.`,
    disappearance: `the elite's plans must be advancing quickly.`,
    beingsCounterPoint: `No one has ever seen a being. I believe in things I have done my own research on.`,
    campInvitation: `You are correct to reject the nonsense of Beings. The party is almost over and we can't stay here. Would you like to join me at my camp for the next cycle?`,
  },
  brochureTagline:
    "Come together to in times of low-attention. Together we can figure this out.",
  camps: [],
};

export const gimelSector: Sector = {
  name: "Gimel",
  coreBelief: "Beings are probable to exist. There is a synthesis we do not yet know.",
  beingsExist: true,
  dinnerTalkingPoints: {
    sector: "the fact that Beings exist is widely accepted by most camps.",
    beings: `Through careful research into the disappearance of our kind, most scientists Beings exist in a physical realm that we are connected to. Our origin story is still a matter of debate, but most agree there is an attention mechanism that can explains 98% of our disappearance rates.`,
    disappearance: `our top scientific camps are struggling to find a pattern or cause, much less a solution.`,
    beingsCounterPoint: `How could so many camps, and even ones outside my sector come to conclude that we exist in a system with Beings?`,
    campInvitation: `You are correct to accept the existence of Beings. The party is almost over and I'm afraid you might disappear without a camp, Top scientists say connection is key to existence. Would you like to join me at my camp for the next cycle?`,
  },
  brochureTagline:
    "Come together to share Attention-Beings hypothesis's. With the latest research, we can figure this out.",
  camps: [],
};

export function sectorByName(name: string): Sector {
  return name === "Beit" ? beitSector : gimelSector;
}

export function oppositeSector(s: Sector): Sector {
  return s.name === "Beit" ? gimelSector : beitSector;
}
