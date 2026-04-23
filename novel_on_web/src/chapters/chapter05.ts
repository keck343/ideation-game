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
import {
  coffee,
  gamer,
  movingTruck,
  playLoop,
  watchFenceVoid,
} from "../data/art";
import type { Sector } from "../data/sectors";
import { beitSector, gimelSector, sectorByName } from "../data/sectors";
import type { Camp } from "../data/camps";

type Handoff = {
  startingSectorName: string;
  nextMove: "skip" | "attend" | "volunteer";
};

function speakerPrefixFor(index: number, title: string): string {
  if (index === 0) return `The first ${title}`;
  if (index % 2 === 0) return `Another ${title}`;
  return `A different ${title}`;
}

function* tellCampsBeliefs(
  sector: Sector,
  speakerTitle: string,
  withUnstated: boolean
) {
  for (let i = 0; i < sector.camps.length; i++) {
    const camp = sector.camps[i];
    const prefix = speakerPrefixFor(i, speakerTitle);
    yield text(
      `${prefix} says that the camp often referred to as ${camp.knownName} believes that ${camp.statedCampCoreBelief}`
    );
    if (withUnstated) {
      yield text(
        `And other ${speakerTitle}s add that ${camp.knownName} also believes ${camp.unstatedCampCoreBelief}`
      );
    }
  }
}

function pickRandom<T>(arr: readonly T[]): T {
  return arr[Math.floor(Math.random() * arr.length)];
}

function sampleTwo<T>(arr: readonly T[]): T[] {
  if (arr.length <= 2) return [...arr];
  const a = Math.floor(Math.random() * arr.length);
  let b = Math.floor(Math.random() * (arr.length - 1));
  if (b >= a) b += 1;
  return [arr[a], arr[b]];
}

export const chapter05: ChapterFactory = function* (stateIn, handoffIn) {
  yield imageBg(5);
  yield imageFg(5);
  yield section(5, "Level 5");

  const handoff = handoffIn as Handoff;
  let chapterSector = sectorByName(handoff.startingSectorName);
  let altSector = chapterSector === beitSector ? gimelSector : beitSector;
  let chapterCamp = chapterSector.camps[0];
  let altCamp = altSector.camps[0];
  const { nextMove: attendance } = handoff;
  let state = stateIn;
  let changeSectors = false;
  let conferenceCamps: Camp[] = [];

  if (attendance === "volunteer") {
    yield text(
      "You arise bright and early at the crack of dawn. Ready to volunteer you get dressed, brush your teeth and grab your bag."
    );
    yield art(gamer);
    yield text(
      "But your friend is no where to be found. You go looking for them, only to find them asleep in their bed."
    );

    const wake = yield* askYn("Do you wake them?");
    let attendYes = true;
    if (wake) {
      yield text(
        "You shake your friend gentle for a few minutes, but then gradually increase the vigor of your shakes until they awake dazed and confused."
      );
      yield text(
        "You tell them that if we are going to make it in time to volunteer they have to get up."
      );
      yield text("They tell you to go ahead and they'll try to catch up.");
      attendYes = yield* askYn("Do you still go early to volunteer?");
    } else {
      yield text(
        "You decide to let your friend sleep and catch the bus to the conference."
      );
    }

    if (attendYes) {
      yield art(coffee);
      yield text(
        "You make it to the conference early and are assigned to set up chairs."
      );
      yield text(
        "While setting out chairs you chat with the other volunteers and learn that there are at least four other major camps in your sector."
      );
      yield text(playLoop);
      yield text(
        `The others call your camp ${chapterCamp.knownName}, though the people in your camp don't like that name.`
      );
      yield text(
        `One of the other volunteers explains that your camps does believe that ${chapterCamp.statedCampCoreBelief}, but not so hidden underneath that is the belief that ${chapterCamp.unstatedCampCoreBelief}`
      );

      const yesAssessment = yield* askYn(
        "Do you think this is an accurate assessment of your camps beliefs?"
      );
      let yesOtherCamps: boolean;
      if (yesAssessment) {
        yield text(
          "You feel relieved that someone said out loud what you suspected all along."
        );
        yesOtherCamps = yield* askYn("Do you ask the other volunteers about their camps beliefs?");
      } else {
        yield text("You tell them that they are misrepresenting what your camp believes.");
        const yesBeliefs = yield* askYn("Are your camp's beliefs your beliefs?");
        if (yesBeliefs) {
          yield text(
            "You say proudly that it is. Everyone returns to setting up chairs."
          );
          yesOtherCamps = false;
        } else {
          yield text(
            "Another volunteer says there's often a lot of confusion about what their camp believes."
          );
          yesOtherCamps = yield* askYn("Do you ask the other volunteers about their camps beliefs?");
        }
      }

      if (yesOtherCamps) {
        yield* tellCampsBeliefs(chapterSector, "volunteer", true);
        yield text(
          "Overwhelmed with information you say you need to go to the bathroom, but really just want an excuse to wonder outside."
        );
        yield text(
          "As you wonder, you see a different kind of fence and a flurry of activity behind it."
        );
        yield art(watchFenceVoid);

        const approachFence = yield* askYn("Do you go up to the fence?");
        if (approachFence) {
          yield text(
            "Someone from the other fence waves at you. It's rare to catch glimpses of people from other sectors, they say. Would you like to join our conference?"
          );
          const choice = yield* askMulti("How do you respond?", [
            { key: "a", label: "Say yes" },
            { key: "b", label: "Politely decline" },
            { key: "c", label: "Decline denouncing their sector" },
            { key: "d", label: "Ask what the difference between their conference and your conference is" },
            { key: "e", label: "Run away" },
          ]);

          if (choice === "a") {
            changeSectors = true;
          } else if (choice === "e") {
            yield text("You run back to the conference just in time to hear the first speakers.");
          } else if (choice === "b") {
            yield text(
              "You thank them for their offer, but must go back to setting up chairs. They wish you luck at your conference and you wish them luck at theirs. You return to the conference just as it's getting started."
            );
          } else if (choice === "c") {
            yield text(
              `You tell them that it ${chapterSector.coreBelief}. They scoff and call you a bigot. Having said your piece, you return to the conference just as it's getting started.`
            );
          } else {
            yield text("You ask what the difference between the conferences is.");
            yield text(
              `They respond, while there's some controversy essentially _your_ conference believes ${chapterSector.coreBelief} But _our_ conference believes ${altSector.coreBelief}.`
            );
            yield text("They ask you what you think and which conference you want to be at.");
            const nextChoice = yield* askMulti("How do you respond?", [
              { key: "a", label: "My conference's belief resonates with me, so I will stay" },
              { key: "b", label: "Your conference's belief resonates with me, so I will switch conferences" },
              { key: "c", label: "I must fulfil my volunteer duties and meet my friend, so I will stay" },
            ]);
            if (nextChoice === "b") {
              changeSectors = true;
            } else if (nextChoice === "c") {
              yield text("You thank them for their offer, but must go back to setting up chairs.");
            }
            if (nextChoice !== "b") {
              yield text(
                "They wish you luck at your conference and you wish them luck at theirs. You return to the conference just as it's getting started."
              );
            }
          }

          if (changeSectors) {
            yield text(
              "You cross over the fence, wondering what this new conference will be like."
            );
            const tmpS = chapterSector;
            chapterSector = altSector;
            altSector = tmpS;
            const tmpC = chapterCamp;
            chapterCamp = altCamp;
            altCamp = tmpC;
          }
        }
      }
    }
  }

  if (attendance !== "skip") {
    yield text(
      "You feel mildly overwhelmed at the number of people, but take your seat to hear the speakers."
    );
    const allSessions = yield* askYn(
      "Each camp at the conference gets a session, do you want to stay for all sessions?"
    );
    if (allSessions) {
      yield* tellCampsBeliefs(chapterSector, "speaker", false);
      conferenceCamps = chapterSector.camps.slice(1);
      yield text("You feel full of knowledge and mildly overwhelmed.");
    } else {
      yield text("You skip in and out of the conference and catch a couple speakers.");
      conferenceCamps = sampleTwo(chapterSector.camps.slice(1));
      yield text(
        `You heard one speaker from the co-called ${conferenceCamps[0].knownName} camp say that their camp believes ${conferenceCamps[0].statedCampCoreBelief}`
      );
      if (conferenceCamps[1]) {
        yield text(
          `You heard one speaker from the co-called ${conferenceCamps[1].knownName} camp say that their camp believes ${conferenceCamps[1].statedCampCoreBelief}`
        );
      }
    }

    let findYes = false;
    if (!changeSectors) {
      findYes = yield* askYn("Do you want to find your friend and discuss the sessions you heard?");
      if (findYes && attendance === "volunteer") {
        yield text(
          "You find your friend and they apologize for oversleeping and ask you if made it in time to volunteer."
        );
        yield text(
          "You say you made it and helped with the chairs, and ask what they thought of the conference."
        );
      } else if (findYes) {
        yield text("You find your your friend and ask what they thought of the speakers.");
      }
    } else {
      yield text(
        "You have the urge to find your friend, but realize they wouldn't be at this sectors conference."
      );
      findYes = yield* askYn("Do you want to search for the person who invited you?");
      if (findYes) {
        yield text(
          "You find them in the tabling area and ask what they thought of the speakers."
        );
      }
    }

    if (findYes) {
      const personCamp = changeSectors
        ? chapterSector.camps[chapterSector.camps.length - 1]
        : chapterCamp;
      yield text(
        `They say that they thought while everyone's heart was in a good place, the only one that made any sense was the one who talked about ${personCamp.statedCampCoreBelief}.`
      );
      yield text(
        "You smile and nod, but find yourself wondering about what the other speakers said."
      );
    }
    yield symbol({ symbol: "√♥-√v--√♥-√v–", numLines: 3 });
  }

  if (attendance === "skip") {
    const choice = yield* askMulti(
      "You wake up to another day in the new low-Attention normal. What do you want to with your day?",
      [
        { key: "a", label: "Your own research at the camp's Library" },
        { key: "b", label: "Read a novel" },
        { key: "c", label: "Find a way of being in service" },
      ]
    );
    if (choice === "a") {
      yield text(
        `After hours of pouring over old newspaper archives, you feel that between all the lines the articles are saying: ${chapterCamp.statedCampCoreBelief} and ${chapterCamp.counterSectorStatement}`
      );
      yield art(watchFenceVoid);
      state = addCamp(state, chapterCamp.knownName);
    } else if (choice === "b") {
      yield text("You find a novel and quite enjoy reading it.");
    } else {
      yield text(
        "You find a group of people cutting up more pamphlets and handing out supplies. It feels satisfying to be doing some concrete."
      );
    }

    yield symbol({ numLines: 5 });
    yield text("Just as you are about to take a lunch break, more headlines come in.");

    const lookAtHeadlines = yield* askYn("Do you look at the headlines?");
    if (lookAtHeadlines) {
      yield text(`The headlines read: ${chapterCamp.secondCrisisExplanation}`);
      yield art(coffee);
      yield text(
        "You are about to eat your lunch when you see your friend depart for the conference."
      );
      const chase = yield* askYn("Do you chase after them?");
      if (!chase) {
        yield text("You turn away to return to your lunch.");
        return {
          toChapter: "chapter06",
          state,
          handoff: {
            startingCampName: chapterCamp.knownName,
            participated: true,
          },
        };
      } else {
        yield text(
          "You chase after them and just catch the last bus before it departs. You arrive at the conference after the speakers have finished."
        );
        conferenceCamps = [];
      }
    } else {
      yield text("You turn away to return to your lunch.");
      return {
        toChapter: "chapter06",
        state,
        handoff: {
          startingCampName: chapterCamp.knownName,
          participated: false,
        },
      };
    }
  }

  yield text(
    "You wonder through the tabling area and wonder how this Attention is an important as everyone says and about where you've been sleeping this whole time."
  );
  yield text(
    "Headlines come raining in saying: Attention drops even further, 10 more reported dead."
  );
  yield symbol({ numLines: 4 });

  yield text(
    "The people tabling look frightened and begin packing up. Contemplating your next move, you realize there there are buses headed back to all the camps."
  );

  let nextCamp = chapterCamp;
  if (!changeSectors) {
    const busChoice = yield* askMulti("Where do you want to take a bus to?", [
      { key: "a", label: "back to your camp" },
      { key: "b", label: "go to a new camp" },
    ]);
    if (busChoice === "a") {
      yield text("You take the bus back to your camp.");
      return {
        toChapter: "chapter06",
        state,
        handoff: {
          startingCampName: chapterCamp.knownName,
          participated: true,
        },
      };
    }
  }

  if (conferenceCamps.length > 0) {
    const options = conferenceCamps.map((c, idx) => ({
      key: String(idx + 1),
      label: `Camp known as ${c.knownName}`,
    }));
    let extraUnknown = false;
    if (conferenceCamps.length + 1 < chapterSector.camps.length) {
      options.push({
        key: String(conferenceCamps.length + 1),
        label: "A camp you've never heard of.",
      });
      extraUnknown = true;
    }
    const campChoice = yield* askMulti("Which camp do you want to take the bus back to?", options);
    yield text("You catch the bus and wonder what awaits you in this new camp.");
    yield art(movingTruck);
    const idx = parseInt(campChoice, 10) - 1;
    if (extraUnknown && idx === conferenceCamps.length) {
      // pick a camp the conference didn't cover
      const covered = new Set(conferenceCamps.map((c) => c.knownName));
      const uncovered = chapterSector.camps.filter(
        (c) => !covered.has(c.knownName) && c.knownName !== chapterCamp.knownName
      );
      nextCamp = uncovered.length > 0 ? pickRandom(uncovered) : pickRandom(conferenceCamps);
    } else {
      nextCamp = conferenceCamps[idx];
    }
  } else {
    yield text("Not knowing what any of the camps are, you pick a bus at random.");
    yield art(movingTruck);
    nextCamp = pickRandom(chapterSector.camps.slice(1));
  }

  return {
    toChapter: "chapter06",
    state,
    handoff: {
      startingCampName: nextCamp.knownName,
      participated: true,
    },
  };
};
