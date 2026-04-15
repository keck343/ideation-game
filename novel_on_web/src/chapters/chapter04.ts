import {
  art,
  askFree,
  askMulti,
  askYn,
  expandIdea,
  imageBg,
  imageFg,
  section,
  symbol,
  text,
  typewriter,
  type ChapterFactory,
} from "../engine/helpers";
import {
  chainsLine,
  fenceVoid,
  floatingHeartGhost,
  playButton,
  playLoop,
} from "../data/art";
import { beitSector, gimelSector, sectorByName } from "../data/sectors";

type Handoff = {
  startingSectorName: string;
  friendType: "alt-believer" | "believer" | "contrarian";
  desiredProduct: string;
};

export const chapter04: ChapterFactory = function* (state, handoffIn) {
  yield imageBg(4);
  yield imageFg(4);
  yield section(4, "Level 4");

  const handoff = handoffIn as Handoff;
  let chapterSector = sectorByName(handoff.startingSectorName);
  let altSector = chapterSector === beitSector ? gimelSector : beitSector;
  let chapterCamp = chapterSector.camps[0];
  let altCamp = altSector.camps[0];
  const { friendType, desiredProduct } = handoff;

  const bonding: string =
    friendType === "alt-believer"
      ? "your mutual distrust in the first camp you visited. You feel so relieved you escaped there and can't imagine having stayed."
      : friendType === "believer"
        ? "your shared work towards a common goal. It feels comforting to be doing something concrete amid the chaos."
        : "your numerous late night debates. It feels comforting to have real discussions and gain a better understanding of this world.";

  yield text(
    `A few weeks have passed and you have enjoyed getting to know your friend. You have bonded over ${bonding}`
  );
  yield text(playLoop.repeat(4));
  yield text(
    "Just when you had settled into a routine, one morning you awake to blaring siren."
  );
  yield symbol({ symbol: chainsLine, numLines: 3 });
  yield text("You are bombarded with the news.");

  const readHeadline = yield* askYn("Do you read the headline?");
  if (readHeadline) {
    yield text(
      `You are surrounded by the headline: ${chapterCamp.initialCrisisHeadline}`
    );
  }

  yield text("You rush to find your friend.");
  if (friendType !== "alt-believer") {
    yield text(
      `Your friend rushes over to you and hands you a ${desiredProduct}, saying Here have the last ${desiredProduct}, it may be a long time before we get more.`
    );
  } else {
    yield text("Your friend rushes over to you, looking scared.");
  }
  yield symbol({ symbol: "( //>///<//)", numLines: 3 });

  const askWhatsHappening = yield* askYn("Do you ask your friend what is going on?");
  if (askWhatsHappening) {
    yield text(
      "You ask your friend what's going on. Surely they must know."
    );
    yield text(
      `Your friend shakes their head and explains: ${chapterCamp.initialCrisisExplanation}`
    );
    yield text("Another person chimes in, Attention is all you need.");
    yield symbol({ symbol: "( //>///<//)", numLines: 2 });
    yield text(
      "You ask, surely there must be a way to survive without Attention? Your friend shakes their head like you are insane."
    );
    yield symbol({ symbol: "( //>///<//)", numLines: 1 });
  }

  const stayWithFriend = yield* askYn("Do you want to stay with your friend to figure out what to do?");
  if (!stayWithFriend) {
    yield typewriter(
      "You turn away from your friend, doubting the person you have formed a bond with. Unsure what to do, you walk to the edge of the camp."
    );
    yield text(
      "You did not realize how far you've wondered when you see the fence at the edge of camp."
    );
    yield art(fenceVoid);

    let sayNext = "";
    if (friendType === "alt-believer") {
      yield text(
        `You see the person from your old camp. You feel embarrassed, but before you turn away they call out: Sorry about earlier, I was having an off day! I found you a ${desiredProduct}.`
      );
      yield symbol({ symbol: "( •̯́ ₃ •̯̀)", numLines: 2 });
      yield text(`You smile and thank them for finding a ${desiredProduct}.`);
      yield symbol({ symbol: "૮ ˶ᵔ ᵕ ᵔ˶ ა", numLines: 2 });
      sayNext = " next";
    } else {
      yield text("You see the other guest from the dinner party that feels so long ago.");
    }

    yield text(
      `Feeling a little unsure what to say${sayNext}, you ask them if they've heard the news.`
    );
    yield text(
      "They nod, saying I can't believe we are living through these times. All our camps survive on Attention."
    );
    yield text("You nod saying, I wish I knew what to do about it.");
    yield symbol({ symbol: "｡°(°¯᷄◠¯᷅°)°｡", numLines: 2 });
    yield text(
      "They say, Our camp is working to figure out what to do. Would you like to come back and we can figure it out together?"
    );

    const accept = yield* askYn("Do you accept their invitation?");
    if (accept) {
      yield art(fenceVoid);
      yield text("You cross over the fence, relieved to be elsewhere.");
      const tmp = chapterSector;
      chapterSector = altSector;
      altSector = tmp;
      const tmpC = chapterCamp;
      chapterCamp = altCamp;
      altCamp = tmpC;
    } else {
      yield text("You thank them for the offer, but decline.");
      yield text("They wish you luck because you'll both need it.");
      yield art(fenceVoid);
      yield text(
        "You turn back towards the center of camp, determined to figure this out. You see your friend and they smile at you. You ask simply, What do we do?"
      );
    }
  } else {
    yield text(
      "You apologize for asking a silly question. You ask simply, What do we do?"
    );
  }

  yield text(
    "Come, they say, let's find the others and brainstorm what to do."
  );
  yield text(
    "As you approach the meeting place, you see everyone is holding a brochure."
  );
  yield art(floatingHeartGhost);
  yield text(
    `A comrade is handing out brochures and calling everyone from this sector to come together ${chapterCamp.brochureSummary}`
  );
  yield text("They offer your friend and you a brochure. You both take one to not be rude.");

  const readBrochure = yield* askYn("Do you read the brochure?");
  if (readBrochure) {
    yield text(
      `You pick up the brochure, and notice the headline. Turning to your friend, you ask: But the headline is '${chapterSector.brochureTagline}'`
    );
    yield symbol({ symbol: playButton, numLines: 2 });
    yield text("Your friend shrugs saying, It's basically the same thing.");
    const agree = yield* askYn("Do you agree that they basically say the same thing?");
    if (!agree) {
      const pointOut = yield* askYn("Do you want to point that out?");
      if (pointOut) {
        yield text(
          "You say that that is clearly an inaccurate summary of the brochure, colored by perspective and not facts. The person looks indignant and is about to walk of when"
        );
      } else {
        yield text("Before you have a chance to question the differences,");
      }
    }
  }

  yield text(
    "Your friend asks when the conference is. The comrade replies, Tomorrow! There's a call for volunteers, but they have to wake up at dawn."
  );

  let newState = state;
  let nextMove: "skip" | "attend" | "volunteer";

  const askVolunteer = yield* askYn("Do you ask if they are going to volunteer?");
  if (askVolunteer) {
    yield text(
      "You ask if they are going to volunteer. They say yes and ask if you'd like to join them."
    );
    const joinThem = yield* askYn("Do you wish to volunteer with them?");
    if (joinThem) {
      yield text(
        "Your friend agrees to volunteer as well. You all decide to retire for the night so you will be awake at dawn."
      );
      nextMove = "volunteer";
    } else {
      yield text(
        "You decline. The other person excuses themselves as they will have a very busy day tomorrow."
      );
      yield text(
        "As soon as they leave you friend turns to you and says, What a nerd! But still do you think we should go to this conference?"
      );
      const agreeConf = yield* askYn("Do you agree to go to the conference?");
      if (agreeConf) {
        yield text(
          "You are relieved your friend does not think less of you. Yes, you say, let's go to the conference at a reasonable hour."
        );
        yield text("Relieved to be doing something, you and your friend retire for the evening.");
        nextMove = "attend";
      } else {
        nextMove = "skip";
        const reasonKey = yield* askMulti("Why do you not want to attend the conference?", [
          { key: "a", label: "Conferences are for nerds" },
          { key: "b", label: "Knowledge is a solo pursuit" },
          { key: "c", label: "Other [type your own answer]" },
        ]);
        let reason: string;
        if (reasonKey === "a") reason = "conferences are for nerds.";
        else if (reasonKey === "b") reason = "knowledge is a solo pursuit.";
        else {
          reason = yield* askFree("Type your answer below.");
          newState = expandIdea(newState, reason);
        }
        yield text(`No thank-you, you reply, I think ${reason}`);
        yield text(
          "Too bad, your friend replies, I guess we will see what tomorrow brings."
        );
      }
    }
  } else {
    yield text(
      "The other person excuses themselves as they will have a very busy day tomorrow."
    );
    yield text(
      "As soon as they leave you friend turns to you and says, Do you think we should go to this conference?"
    );
    const agreeConf = yield* askYn("Do you agree to go to the conference?");
    if (agreeConf) {
      yield text(
        "Yes, you say, let's go to the conference at a reasonable hour."
      );
      yield text("Relieved to be doing something, you and your friend retire for the evening.");
      nextMove = "attend";
    } else {
      nextMove = "skip";
      const reasonKey = yield* askMulti("Why do you not want to attend the conference?", [
        { key: "a", label: "Conferences are for nerds" },
        { key: "b", label: "Knowledge is a solo pursuit" },
        { key: "c", label: "Other [type your own answer]" },
      ]);
      let reason: string;
      if (reasonKey === "a") reason = "conferences are for nerds.";
      else if (reasonKey === "b") reason = "knowledge is a solo pursuit.";
      else {
        reason = yield* askFree("Type your answer below.");
        newState = expandIdea(newState, reason);
      }
      yield text(`No thank-you, you reply, I think ${reason}`);
      yield text(
        "Too bad, your friend replies, I guess we will see what tomorrow brings."
      );
    }
  }

  return {
    toChapter: "chapter05",
    state: newState,
    handoff: {
      startingSectorName: chapterSector.name,
      nextMove,
    },
  };
};
