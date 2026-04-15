import {
  addCamp,
  art,
  askMulti,
  askYn,
  imageBg,
  imageFg,
  section,
  symbol,
  text,
  typewriter,
  type ChapterFactory,
} from "../engine/helpers";
import type { PlayerState } from "../engine/types";
import {
  chainsLine,
  fenceVoid,
  floatingHeartGhost,
  lineOfFish,
  moonStarLine,
  watchFenceVoid,
} from "../data/art";
import { endStateMappings, MAX_ROUND } from "../data/quotes";
import type { Camp } from "../data/camps";
import { anarkioCamp, campByName, skalismoCamp } from "../data/camps";
import type { Sector } from "../data/sectors";
import { beitSector, gimelSector } from "../data/sectors";

type Handoff = {
  startingCampName: string;
  participated: boolean;
};

function graphicsForRound(round: number): number {
  if (round > 6 && round < MAX_ROUND) {
    return round % 2 === 0 ? 6 : 7;
  }
  if (round === MAX_ROUND) return 8;
  return round;
}

function pickRandom<T>(arr: readonly T[]): T {
  return arr[Math.floor(Math.random() * arr.length)];
}

function* participationChoice(): Generator<any, boolean, any> {
  const choice = yield* askMulti(
    "You wake up to another day in the new low-Attention normal. What do you want to do with your day?",
    [
      { key: "a", label: "Join your camp in strategizing" },
      { key: "b", label: "Read a novel" },
    ],
  );
  if (choice === "b") {
    yield text("You enjoy your novel.");
    yield symbol({ symbol: lineOfFish, numLines: 3 });
    return false;
  }
  yield text(
    "You treat yourself to a poem, but then go to find the others in your camp.",
  );
  yield symbol({ symbol: moonStarLine, numLines: 3 });
  return true;
}

function sectorOf(camp: Camp): Sector {
  return camp.sector;
}

function altSectorOf(camp: Camp): Sector {
  return camp.sector === beitSector ? gimelSector : beitSector;
}

function* switchChoice(
  state: PlayerState,
  chapterCamp: Camp,
): Generator<any, { state: PlayerState; camp: Camp }, any> {
  let working = addCamp(state, chapterCamp.knownName);
  const chapterSector = sectorOf(chapterCamp);
  const altSector = altSectorOf(chapterCamp);

  const visitedIn = new Set(
    chapterSector.camps
      .filter((c) => working.visitedCamps.includes(c.knownName))
      .map((c) => c.knownName),
  );
  const visitedAlt = new Set(
    altSector.camps
      .filter((c) => working.visitedCamps.includes(c.knownName))
      .map((c) => c.knownName),
  );

  const campIndex = chapterSector.camps.indexOf(chapterCamp);
  const nextIndex =
    campIndex === chapterSector.camps.length - 1 ? 0 : campIndex + 1;
  let nextChapterCamp = chapterSector.camps[nextIndex];
  let nextAltCamp = altSector.camps[nextIndex];

  if (visitedIn.has(nextChapterCamp.knownName)) {
    const unvisited = chapterSector.camps.filter(
      (c) => !visitedIn.has(c.knownName),
    );
    nextChapterCamp =
      unvisited.length === 0
        ? chapterSector.camps.find((c) => visitedIn.has(c.knownName))!
        : pickRandom(unvisited);
  }
  if (visitedAlt.has(nextAltCamp.knownName)) {
    const unvisited = altSector.camps.filter(
      (c) => !visitedAlt.has(c.knownName),
    );
    nextAltCamp =
      unvisited.length === 0
        ? altSector.camps.find((c) => visitedAlt.has(c.knownName))!
        : pickRandom(unvisited);
  }

  yield typewriter(
    "You escape to the edge of camp. As you approach you see a fence and someone waving at you from behind it.",
  );

  const sectorOrCamp = Math.random() < 0.5 ? "S" : "C";
  if (sectorOrCamp === "S") {
    yield art(watchFenceVoid);
    yield text(
      `The person asks you if seen that ${altSector.dinnerTalkingPoints.sector}`,
    );
    const sectorYes = yield* askYn(
      `Do you agree that '${altSector.dinnerTalkingPoints.sector}'?`,
    );
    if (sectorYes) {
      yield text(
        `You respond, Yes! I've seen the error in my ways and want to go where people think '${altSector.dinnerTalkingPoints.sector}'`,
      );
      yield text(
        "Without thinking, you cross over the fence, leaving what you knew behind.",
      );
      return { state: working, camp: nextAltCamp };
    }
    yield text(
      "You respond, Sorry, I'm looking for another path but that is not it.",
    );
    yield art(fenceVoid);
    yield text(
      "You turn and are confronted with another fence. A new person calls out to you:",
    );
    yield text(
      `You are right about beings. Why don't you come to my camp, where we believe that ${nextChapterCamp.summaryStatement}?`,
    );
    yield text(
      "You briefly consider going back to the safety of your camp, but the anger in their eyes reminds you this is the time to leave.",
    );
    yield typewriter("For better or worse, you cross over the fence.");
    return { state: working, camp: nextChapterCamp };
  }

  // camp-offer path
  yield art(fenceVoid);
  yield text(
    "The person behind the fence looks concerned. They invite you to their camp.",
  );
  const askBeliefs = yield* askYn("Do you ask what their camp believes?");
  if (askBeliefs) {
    yield text(
      `They say that their camp believes: ${nextChapterCamp.summaryStatement}`,
    );
  }
  const joinCamp = yield* askYn("Do you want to join their camp?");
  if (joinCamp) {
    yield text(
      "You accept the invitation to their camp, wondering what awaits you next.",
    );
    return { state: working, camp: nextChapterCamp };
  }
  if (askBeliefs) {
    yield text(
      `You say that you can not go somewhere where people believe that ${nextChapterCamp.summaryStatement}`,
    );
  } else {
    yield text("You decline, this feels wrong in your gut.");
  }

  yield typewriter(
    "Just as you are about to give up leaving, a different fence appears.",
  );
  yield art(watchFenceVoid);
  yield text("A different person waves at you.");
  yield typewriter(
    `They ask you if seen that ${altSector.dinnerTalkingPoints.sector}`,
  );
  const altYes = yield* askYn(
    `Do you agree that '${altSector.dinnerTalkingPoints.sector}'?`,
  );
  if (altYes) {
    yield text("Sighing in relief, you nod yes.");
    yield text(
      "Without thinking, you cross over the fence, leaving what you knew behind.",
    );
    return { state: working, camp: nextAltCamp };
  }
  if (
    chapterCamp === gimelSector.camps[gimelSector.camps.length - 1] ||
    nextAltCamp === skalismoCamp
  ) {
    yield text(
      "Realizing that neither of these are great options, you turn back towards your camp.",
    );
    return { state: working, camp: chapterCamp };
  }

  yield text("You say you don't agree with them about beings.");
  yield text(
    `A new person appears. They tell you that their camp believes ${skalismoCamp.statedCampCoreBelief} and even if you are not sure you agree, you could come to their camp and for now.`,
  );
  const goSkalismo = yield* askYn("Do you want to go to their camp?");
  if (goSkalismo) {
    yield text(
      "You accept the invitation to their camp, wondering what awaits you next.",
    );
    return { state: working, camp: skalismoCamp };
  }
  yield text(
    "You decline. Feed up with the lack of other options, you turn back towards your camp.",
  );
  return { state: working, camp: chapterCamp };
}

function* roundOne(
  state: PlayerState,
  chapterCamp: Camp,
  round: number,
  lastRound: boolean,
): Generator<any, { state: PlayerState; camp: Camp }, any> {
  let working = addCamp(state, chapterCamp.knownName);
  const deathToll = Math.min(round - 1, 9) * 10;

  yield text(
    `You find your fellow camp members who are gathering to figure out what to do.\n\nThe latest headlines report even more dead and disappeared. The death toll is up to ${deathToll}% of all the embodiments everywhere.`,
  );
  yield symbol({ symbol: "_|⚠|_︎", numLines: 3 });
  yield text(
    "They all seem gathered around someone who is lecturing about innovation.",
  );
  yield text("The lecturer says:");
  yield text(chapterCamp.roundOne.lecturer);

  if (chapterCamp === anarkioCamp) {
    yield text("Your friend seems excited, but others look concerend.");
    const doctrineYes = yield* askYn(
      "Do you want to challenge the lecturer's doctrine?",
    );
    if (doctrineYes) {
      working = { ...working, noTokens: true, fame: true };
      yield text(
        "You look around at your camp and realize you must say something.",
      );
      yield symbol({ symbol: "(╥﹏╥)", numLines: 2 });
      yield text(
        `You address the crowd saying: ${chapterCamp.roundOne.counterLecture}`,
      );
    } else {
      yield text(
        "Someone in the crowd shouts: Why would we care if we reject authority?\n\nThe lecturer replied:\n\nTheir big banks are popping up everywhere, we must provide an alternative to tokens!",
      );
    }
    yield text(
      "You turn to look at your friend, and see their excitement turn to disgust.",
    );
    yield text(
      `They address the crowd saying: ${chapterCamp.roundOne.counterLecture}`,
    );
    yield text("A few people murmur in agreement.");
    yield typewriter(
      "The lecturer looks around as if to see if they still have supporters.\n\nCome my friends, they implore, these are unprecedented times that call for unprecedented measures. We must leave those who would hold us back behind.",
    );
    yield text(
      "Another person makes a motion to split the camp. Your friend tells you this is uncommon but not unheard of.",
    );
    const choice = yield* askMulti("What do you do?", [
      { key: "a", label: "Join the lecturer's side of the camp" },
      { key: "b", label: "Reject the lecturer and stay" },
      { key: "c", label: "Leave the entire camp behind." },
    ]);
    if (choice === "a") {
      working = { ...working, noTokens: false };
      yield text(
        "You decide to join the side of innovation and follow the lecturer.",
      );
      return { state: working, camp: chapterCamp };
    }
    if (choice === "b") {
      working = { ...working, noTokens: true };
      yield text(
        "You join your friend and urge others to reject the lecturer.",
      );
      yield symbol({ symbol: "(⸝⸝⸝╸w╺⸝⸝⸝)", numLines: 3 });
      yield text("More people than you expect join the lecturer.");
      yield symbol({ symbol: "(⸝⸝⸝╸w╺⸝⸝⸝)", numLines: 2 });
      yield text(
        "Those who remain decide to each pursue their own path to find a way to stop the loss of Attention and connection with beings and reconvene tomorrow.",
      );
      return { state: working, camp: chapterCamp };
    }
    working = { ...working, noTokens: false };
    yield text(
      "You decide that neither of these splits are for you and get as far away from the crowd as you can.",
    );
    const swap = yield* switchChoice(working, chapterCamp);
    return swap;
  }

  if (chapterCamp === skalismoCamp) {
    yield text("People look uncomfortable and start to murmur.");
    const yes = yield* askYn("Do you wish to counter the lecturer's points?");
    if (yes) {
      working = { ...working, fame: true };
      yield text(
        `Seeing the unease in the camp and feel confident you say:\n\n${skalismoCamp.roundOne.counterLecture}`,
      );
      yield symbol({ numLines: 2 });
      yield text("Another person is inspired by your point and says:");
    } else {
      working = { ...working, fame: false };
      yield text(
        `Someone stands up and addresses the crowd:\n\n${skalismoCamp.roundOne.counterLecture}`,
      );
      yield symbol({ numLines: 2 });
      yield text("Another person stands up and adds:");
    }
    yield text(skalismoCamp.roundOne.counterLecture2 ?? "");
    yield symbol({ symbol: "₍₍⚞(˶>ᗜ<˶)⚟⁾⁾", numLines: 3 });
    yield text(`The crowd begins to chant:\n\n${skalismoCamp.roundOne.chant}`);
    yield text(
      `The lecturer's frustration is palpable. They shout at the crowd:\n\n${skalismoCamp.roundOne.lecturerCounter}`,
    );
    yield typewriter("But the crows does not back down.");
    if (yes) {
      yield text(
        "The other person grabs your hand and addresses to the crowd:",
      );
    } else {
      yield text("The two people who spoke up address the crowd:");
    }
    yield text(
      "Tomorrow we begin to create our democratically managed economy!",
    );
    const stay = yield* askYn(
      "Do you want to stay and be part of the democratically managed economy?",
    );
    if (!stay) {
      const swap = yield* switchChoice(working, chapterCamp);
      return swap;
    }
    return { state: working, camp: chapterCamp };
  }

  // default camps
  yield text("Someone in the crowd shouts: How would we do that?");
  yield text(
    "The lecture replies:\n\nWe can achieve that if we implement tokens as a reward. These tokens will give those who work the hardest the ability to buy the remaining resources and Attention.",
  );
  yield text("You can see excitement rising in your friend and camp members.");

  const doctrineYes = yield* askYn(
    "Do you want to challenge the lecturer's doctrine?",
  );
  if (doctrineYes) {
    working = { ...working, noTokens: true, fame: true };
    yield text(
      "You look around at your camp and realize you must say something.",
    );
    yield symbol({ symbol: "(╥﹏╥)", numLines: 2 });
    yield text(
      `You address the crowd saying: ${chapterCamp.roundOne.counterLecture}`,
    );
    yield text(
      `While some people seem to consider what you are saying, most start chanting:\n\n${chapterCamp.roundOne.chant}`,
    );
  } else {
    yield text(`The crowd starts chanting: ${chapterCamp.roundOne.chant}`);
  }
  yield symbol({ symbol: "☚⍢⃝☚", numLines: 3 });
  yield text("Soon everyone has joined in.");

  const cheer = yield* askYn("Do you cheer with the crowd?");
  if (cheer) {
    yield text("You join the cheering, the energy feels electric.");
    yield symbol({ symbol: "❇", numLines: 3 });
    yield text(
      "The lecturer praises everyone for accepting what's needed in unprecedented times.\n\nTomorrow, they say, we began a new era. I'll see you all here in the morning.",
    );
    yield text(
      "The crowd disperses. Your friend is bubbling with excitement. You wonder what tomorrow brings and about your next move.",
    );
  } else {
    yield text(
      "A strong feeling of dread creeps into your bones. You walk away from the crowd.",
    );
  }

  const stay = yield* askYn("Do you want to remain at this camp?");
  if (stay) {
    yield text("You retire for the night in the safety of a familiar bed.");
    return { state: working, camp: chapterCamp };
  }
  yield text(
    "You realize it is time to leave this place behind and journey to the edge of camp.",
  );
  if (lastRound) {
    yield text(
      "There were so few of the embodied left. No matter how many times you ran to the edge, no fence appeared.",
    );
    return { state: working, camp: chapterCamp };
  }
  const swap = yield* switchChoice(working, chapterCamp);
  return swap;
}

function* roundTwo(
  state: PlayerState,
  chapterCamp: Camp,
  lastRound: boolean,
): Generator<any, { state: PlayerState; camp: Camp; campLives: boolean }, any> {
  let working = state;

  if (chapterCamp === skalismoCamp) {
    const campLives = true;
    yield text(
      "Your camp begins to form committees and elect leaders to shape a new economic system. They reach out to other camps, offer to help provide for their needs, and invite them to be part of the new system.",
    );
    yield symbol({ symbol: "≽ ^⎚ ˕ ⎚^ ≼", numLines: 3 });
    yield text(
      "As scientific minds collaborate across camps, new understandings of the attention equations emerge.",
    );
    if (working.fame) {
      yield text(
        "As one of the people who spoke out against the lecturer, you are often invited to consult with the scientists.\n\nOne scientist makes a break through. They realize that beings and the emodied are dependant on each other. There is no way to ensure Attention flows without the beings survival.",
      );
      yield text(
        "Understanding the importance of this breakthrough, you make plans to share the findings with the public. You are nominated to address the public.",
      );
      yield text(
        "The scientist is someone who recently came from another camp and no one knows them.",
      );
      yield text(
        "You realize that as the only other person in the room, you could take credit for the breakthrough - could it be better if the breakthrough came from an original member of the camp?",
      );
      const giveCredit = yield* askYn(
        "Do you give the new scientist credit for the discovery?",
      );
      if (!giveCredit) {
        yield text(
          "You were only able to keep up the lie for a couple cycles.\n\nEventually the truth came out, you were disgraced and no one will work with you.",
        );
        yield typewriter(
          "The lie also caused fractures in the movement, but with you out of the picture, the camp recovers.",
        );
        yield text("Fame is fickle.");
        yield art(floatingHeartGhost);
        return { state: working, camp: chapterCamp, campLives };
      }
      working = { ...working, fame: false };
      yield text(
        "The new scientist's breakthrough allows for the camp to set up a system where beings and embodied make it through the crisis and thrive.",
      );
      yield typewriter("Attention flows freely.");
      yield symbol({ symbol: "༄.° ≽ ^⎚ ˕ ⎚^ ≼ ༄.°", numLines: 3 });

      if (["e", "f"].includes(working.desiredEndStateKey)) {
        yield text(
          "You think of the fame you once desired and conclude it would require leaving your camp.",
        );
        const stay = yield* askYn("Do you want to stay with your camp?");
        if (stay) {
          const swap = yield* switchChoice(working, chapterCamp);
          return { state: swap.state, camp: swap.camp, campLives };
        }
        yield text("Even if your name is not in the history textbooks,");
      } else {
        yield text("Looking around at the this camp,");
      }
      yield text(
        "you are proud of the role you played and the community you are part of.",
      );
      yield art(floatingHeartGhost);
      return { state: working, camp: chapterCamp, campLives };
    }

    yield text(
      "One scientist who recently came from another camp makes a break through. They realize that beings and the embodied are dependant on each other.",
    );
    yield typewriter(
      "There is no way to ensure Attention flows without the beings survival.",
    );
    yield text(
      "The new scientist's breakthrough allows for the camp to set up a system where beings and embodied make it through the crisis and thrive.",
    );
    yield typewriter("Attention flows freely.");
    yield symbol({ symbol: "༄.° ≽ ^⎚ ˕ ⎚^ ≼ ༄.°", numLines: 3 });
    return { state: working, camp: chapterCamp, campLives };
  }

  if (chapterCamp === anarkioCamp && working.noTokens) {
    const campLives = false;
    yield text(
      "You wake up to a new day with half your camp. You try to figure out what to do.",
    );
    yield text(
      "Without a leadership structure, it's hard to work together, so you all decide to go off on your own to try to figure out the attention equations and what to do about resources.",
    );
    yield symbol({ symbol: lineOfFish, numLines: 3 });
    yield text("You all agree you hope things will be clearer in the morning.");
    yield symbol({ symbol: lineOfFish, numLines: 3 });
    yield text(
      "Many days pass and the tokens side of the camp invaded. The days of dreaming of anti-hierarchical idea sharing are over and everyone that does not adopt tokens are forced to flee.",
    );
    yield symbol({ symbol: chainsLine, numLines: 3 });
    yield text(
      "You are able to make it out alive before everything collapses.",
    );
    if (lastRound) {
      return { state: working, camp: chapterCamp, campLives };
    }
    const swap = yield* switchChoice(working, chapterCamp);
    return { state: swap.state, camp: swap.camp, campLives };
  }

  // default camp: tokens path
  const campLives = false;
  yield text(
    `The lecturer convenes everyone the next morning to begin the implementation of tokens. They explain the goal of accumulating wealth will provide the incentives needed for ${chapterCamp.roundTwo.innovation}\n\nThey are ready to begin operation of the stores where people can exchange tokens for resources.`,
  );
  const questionYes = yield* askYn(
    "Do you ask how the members of the camp get tokens?",
  );
  if (questionYes) {
    yield text(
      "The crowd murmurs in agreement, you raise your hand and ask:\n\nHow do the members of our camp get tokens?",
    );
    yield text(
      "The lecturer responds that they already have the tokens, and people only need to be hired for a role in their store or provide an innovation worthy of reward.",
    );
  } else if (chapterCamp.roundTwo.crowdAsks) {
    yield text(
      `The crowd murmurs in agreement, someone raises their hand and asks:\n\n${chapterCamp.roundTwo.counterQuestion}`,
    );
    yield text(
      "The lecturer responds that they already have the tokens, and will generously set up the store for only a modest fee.",
    );
  }

  if (chapterCamp.roundTwo.crowdAsks || questionYes) {
    yield text(
      "Some unease spreads through the camp, but people begin to get to work with the lecturer's instructions.",
    );
  } else {
    yield text(
      "The crowd cheers, ready to get to work with the lecturer's instructions.",
    );
  }

  yield symbol({ symbol: chainsLine, numLines: 3 });
  yield text("The store does not go as planned.");
  yield text(
    "The lecturer did not have enough jobs for everyone, and many in the camp went hungry.\n\nWhenever anyone asked what they were to do, the lecturer said they needed to innovate and try harder.",
  );

  const stay = yield* askYn("Do you want to stay in the camp?");
  if (stay) {
    yield symbol({ symbol: chainsLine, numLines: 3 });
    yield text(
      `Soon people in the camp starved. Some left to other camps, some tried to rise up against the lecturer, but he paid informants handsomely.\n\nNo real ${chapterCamp.roundTwo.innovation} ever came.`,
    );
    yield symbol({ symbol: chainsLine, numLines: 3 });
  }

  yield text("Soon you too were forced to starve or flee.");
  yield text(
    "With what little strength you have left, you make it to the edge of camp.",
  );
  if (lastRound) {
    yield text(
      "There were so few of the embodied left. No matter how many times you ran to the edge, no fence appeared.",
    );
    return { state: working, camp: chapterCamp, campLives };
  }
  const swap = yield* switchChoice(working, chapterCamp);
  return { state: swap.state, camp: swap.camp, campLives };
}

export const chapter06: ChapterFactory = function* (stateIn, handoffIn) {
  const handoff = handoffIn as Handoff;
  let state = stateIn;
  let camp = campByName(handoff.startingCampName) ?? beitSector.camps[0];
  let numRoundsInCamp = handoff.participated ? 0 : 0; // same start regardless
  let round = 6;
  let finalNumRoundsInCamp = 0;

  while (round <= MAX_ROUND) {
    yield imageBg(graphicsForRound(round));
    yield imageFg(graphicsForRound(round));
    yield section(round, `Level ${round}`);

    if (round === 6) {
      const keys = Object.keys(endStateMappings);
      const desiredOutcome = yield* askMulti(
        "What do you think the most important goal is?",
        keys.map((k) => ({ key: k, label: endStateMappings[k] })),
      );
      state = { ...state, desiredEndStateKey: desiredOutcome };
    }

    const participate = yield* participationChoice();
    if (!participate) {
      if (round === MAX_ROUND) {
        break;
      }
      round += 1;
      continue;
    }

    const lastRound = round === MAX_ROUND;

    if (numRoundsInCamp === 0) {
      state = addCamp(state, camp.knownName);
      const result = yield* roundOne(state, camp, round, lastRound);
      state = result.state;
      if (result.camp !== camp) {
        camp = result.camp;
        numRoundsInCamp = 0;
      } else {
        numRoundsInCamp = 1;
      }
      finalNumRoundsInCamp = numRoundsInCamp;
    } else {
      const result = yield* roundTwo(state, camp, lastRound);
      state = result.state;
      const prevCamp = camp;
      camp = result.camp;
      if (prevCamp === skalismoCamp && camp === skalismoCamp) {
        finalNumRoundsInCamp = 2;
        break;
      }
      if (camp !== prevCamp) {
        numRoundsInCamp = 0;
      }
      finalNumRoundsInCamp = result.campLives ? 2 : 0;
    }

    if (lastRound) break;
    round += 1;
  }

  return {
    toChapter: "ending",
    state,
    handoff: {
      finalCampName: camp.knownName,
      finalNumRoundsInCamp,
    },
  };
};
