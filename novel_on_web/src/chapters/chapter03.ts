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
import { fenceVoid, lockAndKey, penguinsAndSkull } from "../data/art";
import { beitSector, gimelSector, sectorByName } from "../data/sectors";

type Handoff = { startingSector: string };

export const chapter03: ChapterFactory = function* (state, handoff) {
  yield imageBg(3);
  yield imageFg(3);
  yield section(3, "Level 3");

  const startingSectorName = (handoff as Handoff).startingSector ?? "Beit";
  const chapterSector = sectorByName(startingSectorName);
  const altSector = chapterSector === beitSector ? gimelSector : beitSector;
  const chapterCamp = chapterSector.camps[0];
  const altCamp = altSector.camps[0];

  yield text(
    "You wake up for a fresh day in your new camp, relieved to have escaped nonexistence even for just a night."
  );
  yield art(penguinsAndSkull);
  yield text(
    "Not totally sure what to make of this new day, you set out to find caffeine."
  );

  const caffeineChoice = yield* askMulti("Which form of caffeine do you crave today?", [
    { key: "a", label: "Coffee" },
    { key: "b", label: "Tea" },
    { key: "c", label: "Soda Pop" },
    { key: "d", label: "No need for stimulants - Refreshing Sparkling Water" },
    { key: "e", label: "No need for bubbles - Purified Still Water" },
    { key: "f", label: "Just any caffeine please" },
  ]);

  const desiredProduct: string = (() => {
    switch (caffeineChoice) {
      case "a": return "coffee";
      case "b": return "tea";
      case "c": return "soda pop";
      case "d": return "sparkling water";
      case "e": return "purified water";
      default: return "XL dunkin donuts iced coffee";
    }
  })();

  yield text(
    `You see the embodiment from the party. Hoping they will continue to be a good host, you walk over and inquire, Do you know where I could find a ${desiredProduct}?`
  );
  yield text("(｡ᵕ ◞ _◟)");
  yield typewriter(
    `They look up at you with a grim face. You really haven't been around much have you? There hasn't been ${desiredProduct} in many cycles. I guess you did conclude quote: '${state.ideaDescription}'`
  );
  yield text(
    `They sigh and say: Come, let's meet with the others to figure out what do about the lack of ${desiredProduct} these days.`
  );

  let crossedToAlt = false;
  let outcomeSet = false;
  let friendType: "alt-believer" | "believer" | "contrarian" = "believer";
  let endingCampName = chapterCamp.knownName;

  const follow = yield* askYn("Do you follow them to meet with the others?");
  if (!follow) {
    yield text(
      "Annoyed by their arrogance, you wonder in the opposite direction. You begin to see the edge of the camp emerge, with a fence unlike any you've ever seen."
    );
    yield art(fenceVoid);
    yield text(
      "It feels impenetrable, yet you can see the other party guest on the other side and wave at them."
    );
    yield text("(っᵔ◡ᵔ)っ");
    yield text(
      `They wave back and ask, how is '${state.ideaDescription}' going for you?`
    );

    const mockChoice = yield* askMulti("In response do you:", [
      { key: "a", label: "tear up silently" },
      { key: "b", label: "express your frustration" },
      { key: "c", label: "lash out at them for mocking you" },
    ]);

    if (mockChoice === "a") {
      yield text(
        "They look at you kindly and say, I totally understand. Everyone is feeling it these days and no one is what they seem. Would you like to come to my camp?"
      );
      yield art(fenceVoid);
      const go = yield* askYn("Would you like to go with them?");
      if (go) {
        yield text(
          "You wipe the tears from your face and nod. You both smile, and without even knowing how you cross the threshold."
        );
        crossedToAlt = true;
        friendType = "alt-believer";
        endingCampName = altCamp.knownName;
        outcomeSet = true;
      } else {
        yield text(
          "You wipe the tears from your face and say: Thank you for your offer, but there's been too much change lately and I'm going to try to stick it out here."
        );
        yield symbol({ symbol: "^", numLines: 3 });
        yield text("They wish you luck and take their leave.");
        yield text("Resigned to make things work, you turn back towards the others.");
      }
    } else if (mockChoice === "b") {
      yield text(
        "You turn to them and say exasperatedly: How do you know what you're talking about?!? How do any of us know what we are talking about?!"
      );
      yield text(
        `They look at you sympathetically and say: ${altCamp.counterSectorStatement}`
      );
      const apologize = yield* askYn("Do you apologize for expressing frustation?");
      if (apologize) {
        yield text(
          `You say, I'm sorry, it's been a confusing morning, and I really just needed a ${desiredProduct}.`
        );
        yield text(
          "They nod saying, I totally understand. Would you like a break from all this? Do you want to come to my camp?"
        );
        const go = yield* askYn("Would you like to go with them?");
        if (go) {
          yield text("Without even knowing how you cross the threshold.");
          yield art(fenceVoid);
          crossedToAlt = true;
          friendType = "alt-believer";
          endingCampName = altCamp.knownName;
          outcomeSet = true;
        } else {
          yield art(fenceVoid);
          yield text(
            "You say: Thank you for your offer, but there's been too much change lately and I'm going to try to stick it out here."
          );
          yield symbol({ symbol: "^", numLines: 3 });
          yield text("They wish you luck and take their leave.");
          yield text("Resigned to make things work, you turn back towards the others.");
        }
      } else {
        yield text(
          "You decide it is not worth engaging in further conversation and return to camp."
        );
      }
    } else {
      yield text(
        "You turn to them and say exasperatedly: How do you know what you're talking about?!? You're such an arrogant prick!"
      );
      yield text(
        `They look at you exacerbated. Do you really want to condemn yourself to a camp without ${desiredProduct}?`
      );
      yield text(`How do you know I like ${desiredProduct}?`);
      yield text(
        "Walls are thin, they laugh. Maybe when you've come to your senses you'll want to pass through them."
      );
      yield symbol({ symbol: '(¬_¬")', numLines: 3 });
      yield art(fenceVoid);
      yield text(
        "Determined to prove them wrong, you say nothing and turn back towards the others."
      );
    }
  }

  if (outcomeSet) {
    // crossed through the fence; skip camp rally
    const newState = addCamp(state, endingCampName);
    return {
      toChapter: "chapter04",
      state: newState,
      handoff: {
        startingSectorName: crossedToAlt ? altSector.name : chapterSector.name,
        friendType,
        desiredProduct,
      },
    };
  }

  // camp rally
  let newState = addCamp(state, chapterCamp.knownName);

  yield text(
    "As you walk towards the others, you see many people fluttering around with different diagrams, charts, and statistics."
  );
  yield symbol({ symbol: "(╯ ͠° ͟ʖ ͡°)╯┻━┻", numLines: 3 });
  yield typewriter(
    "Someone turns to you, clutching their diagrams close to their chest. They implore you, What is to be done?"
  );

  const leninOpinion = chapterSector.name === "Gimel" ? "no " : "";
  yield text(
    `Another person turns to them whispering, Don't be like that traitor! Died at 53 in a coma and for ${leninOpinion}good reason.`
  );
  yield text("They clutch their diagrams closer to their chest, fear in their eyes.");
  yield symbol({ symbol: "⤷ ゛ ˎˊ˗", numLines: 2 });
  yield text(
    "Emerging out of the chaos, one person climbs on a chairs and clears their throat. The stirring dies down as people turn towards them."
  );
  yield typewriter(
    "They begin to address the crowd saying:\n\nFellow camp members, these are unprecedented times. We can not even eat breakfast as we used to. Where has all the coffee, tea, and sparkling water gone? What will become of our way of life?"
  );
  yield symbol({ symbol: "ᕙ(  •̀ ᗜ •́  )ᕗ", numLines: 3 });
  yield typewriter(
    `But fear not, we know that ${chapterCamp.summaryStatement}`
  );
  yield typewriter("The crowd cheers.");
  yield art(lockAndKey);

  const cheer = yield* askYn("Do you cheer with the crowd?");
  if (cheer) {
    yield text(
      "Unsure if you believe the speaker or this is just the wisest thing to do, you join the crowd cheering."
    );
    yield typewriter(
      "The speaker clears his throat. Fellow comrades, let's get to work!"
    );
    yield text(
      "Unsure of what to do, you look around anxiously. As your eyes complete their dart around the room, someone gestures at you to come over."
    );
    const gesture = yield* askYn("Do you go over to them?");
    if (gesture) {
      yield text(
        "You walk over to the person gesturing you. They smile and invite you to help them cut up pamphlets."
      );
      yield text(
        "You inquire what the pamphlets are for. They respond, Excellent Question!"
      );
      yield text("(´｡• ◡ •｡`) ♡");
      const slogan0 = chapterCamp.pamphletSlogans[0] ?? chapterCamp.statedCampCoreBelief;
      yield text(slogan0);
      const askWhy = yield* askYn(`Do you ask why the group must '${slogan0}'?`);
      if (askWhy) {
        const slogan1 = chapterCamp.pamphletSlogans[1] ?? chapterCamp.unstatedCampCoreBelief;
        yield text(
          `They seem less excited at your second question, and continue: Well of course, ${slogan1}`
        );
        yield text(
          "You smile uneasily and point out that they are just reading what the pamphlet says."
        );
        yield text("∘ ∘ ∘ ( °ヮ° )");
        yield text(
          "Another person interjects: Some people can only just read the propaganda. Why don't we have an actual discussion over here?"
        );
        yield text(".·°՞(ᗒ□ᗕ)՞°·.");
        yield text("You smile and follow them to their workbench.");
        yield symbol({ symbol: ".·°՞(ᗒ□ᗕ)՞°·.", numLines: 3 });
        friendType = "contrarian";
      } else {
        yield text(
          "You smile to be polite and begin to help cut pamphlets someone just handed you."
        );
        yield text("ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ");
        yield text(
          "As you settle into a rhythm with cutting, you began to feel more at ease with your surroundings and companion."
        );
        yield text("ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ");
        yield text("Pleasant conversation ensues and you feel less alone with a new friend.");
        yield symbol({ symbol: "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ", numLines: 3 });
        friendType = "believer";
      }
    } else {
      yield text(
        "You smile to be polite and begin to help cut pamphlets someone just handed you."
      );
      yield text("ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ");
      yield text("Pleasant conversation ensues and you feel less alone with a new friend.");
      yield symbol({ symbol: "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ", numLines: 3 });
      friendType = "believer";
    }
  } else {
    yield text(
      "You do not join in and feel uneasy surrounded by so many people who would just go along with generic statements."
    );
    yield symbol({ symbol: "(๑•́ -•̀)", numLines: 3 });
    yield typewriter(
      "As you are about to despair, you turn around to see someone else who is also not clapping."
    );
    yield symbol({ symbol: "(๑•́ -•̀)", numLines: 2 });
    yield text(
      "They spot you and you relief wash over their face. They walk over towards you. You smile as they approach."
    );
    yield text("(๑•́(੭˃ᴗ˂)੭•̀)");
    yield text("ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ");
    yield text(
      "They invite you to get out of here and find a better part of camp. You smile and follow them."
    );
    yield symbol({ symbol: "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ", numLines: 3 });
    friendType = "contrarian";
  }

  return {
    toChapter: "chapter04",
    state: newState,
    handoff: {
      startingSectorName: chapterSector.name,
      friendType,
      desiredProduct,
    },
  };
};
