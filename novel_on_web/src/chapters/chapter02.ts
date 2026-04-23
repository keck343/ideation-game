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
import { chapterTwoArt, chapterTwoEndArt } from "../data/art";
import { beitSector, gimelSector } from "../data/sectors";

export const chapter02: ChapterFactory = function* (state, _handoff) {
  yield imageBg(2);
  yield imageFg(2);
  yield section(2, "Level 2");

  yield art(chapterTwoArt);
  yield text(
    "You are at the dinner party. The characters that brought you here have long abandoned you for their friends. You are overwhelmed with social anxiety and questions about where you are and who you are. What course of action will you take?"
  );

  const approach = yield* askYn("Do you want to approach a dinner party guest?");
  let firstSpeaker: typeof beitSector;
  let secondSpeaker: typeof beitSector;
  if (approach) {
    firstSpeaker = beitSector;
    secondSpeaker = gimelSector;
    yield text(
      "You walk over to the nearest dinner party guest and ask what they are discussing. They smile at you and say, why"
    );
  } else {
    firstSpeaker = gimelSector;
    secondSpeaker = beitSector;
    yield text(
      "You stare off into space a little while longer. A party guest approaches you and asks if you are new here. You say yes, and they invite you to join the conversation saying,"
    );
  }

  yield text(
    `we are discussing how ${firstSpeaker.dinnerTalkingPoints.sector}...`
  );
  yield text(
    `The other guest interjects, which is of course preposterous, ${secondSpeaker.dinnerTalkingPoints.sector}`
  );

  const choice = yield* askMulti("Would you like to:", [
    { key: "a", label: "smile and nod" },
    { key: "b", label: "inquire what Beings are" },
    { key: "c", label: "inquire how to leave the party" },
  ]);

  if (choice === "b") {
    yield text(
      `You ask what Beings are. The first guest says:\n\n${firstSpeaker.dinnerTalkingPoints.beings}`
    );
    yield symbol({ symbol: "｡ •̀ _ •́ ｡", numLines: 3 });
    yield text(
      `The second guest looks furious and interjects:\n\n${secondSpeaker.dinnerTalkingPoints.beings}`
    );
    yield symbol({ symbol: "｡ •̀ _ •́ ｡", numLines: 3 });
    yield text(
      "You inquire to what fate Beings might control. The first guests clears their throat and says,"
    );
    yield symbol({ symbol: "( ｡ •̀ _ •́ ｡ )", numLines: 1 });
  }

  if (choice === "c") {
    yield text(
      "You inquire how to leave the party. Both guests look at you alarmed. The first exclaims, it's not safe out there! Haven't you heard?"
    );
    yield symbol({ symbol: "( ｡ •̀ _ •́ ｡ )", numLines: 1 });
    const admit = yield* askYn("Do you admit you have not heard what they are talking about?");
    if (admit) {
      yield text(
        "You confess to being new here. Both express sympathy and remark they miss being young, and fear for your survival because"
      );
    } else {
      yield text(
        "The second guest asks you what you your take on the situation. You stumble, and start to mumble ... The first guest roles their eyes and butts in, saying obviously,"
      );
    }
  }

  if (choice === "a") {
    yield text(
      "You smile and nod, zoning out on the conversation until you hear the first being say,"
    );
  }

  yield text(
    "We have been disappearing across all camps and sectors at alarming rates."
  );

  yield typewriter(
    `${firstSpeaker.dinnerTalkingPoints.disappearance}\n\nThe second guest jumps in saying: This is ludicrous. Clearly ${secondSpeaker.dinnerTalkingPoints.disappearance}`
  );

  yield typewriter("You sense the anger rising up in both guests.");
  yield symbol({ symbol: "( ｡ •̀ ᴖ •́ ｡)", numLines: 3 });
  yield typewriter(
    `The second guest continues, ${secondSpeaker.dinnerTalkingPoints.beingsCounterPoint}`
  );
  yield symbol({ symbol: "୧(๑•̀ᗝ•́)૭", numLines: 2 });
  yield typewriter(
    `The first guest interjects, ${firstSpeaker.dinnerTalkingPoints.beingsCounterPoint}`
  );
  yield symbol({ symbol: "୧(๑•̀ᗝ•́)૭( ｡ •̀ ᴖ •́ ｡)", numLines: 1 });

  yield text("You find yourself faced with a choice.");
  const beingsExist = yield* askYn("Do you believe Beings are likely to exist?");

  let inviterName: string;
  if (beingsExist) {
    yield text(
      "Without thinking you mutter under your breath: peer-reviewed statistics seem reasonable."
    );
    yield typewriter(
      "Both guests now turn their attention to you. One makes an audible sigh of frustration, but appears to be regaining their composure."
    );
    yield text("The other smiles and says:");
    yield text(gimelSector.dinnerTalkingPoints.campInvitation);
    inviterName = gimelSector.name;
  } else {
    yield text("Without thinking you say out loud, Beings seem like a fairy tale.");
    yield typewriter(
      "One guest rolls their eyes with a smug look of superiority on their face, but quickly regains their calm composure."
    );
    yield text("The other smiles and says:");
    yield text(beitSector.dinnerTalkingPoints.campInvitation);
    inviterName = beitSector.name;
  }

  let nextSectorName: string;
  const acceptFirst = yield* askYn("Do you accept the guest's invitation?");
  if (acceptFirst) {
    yield text(
      "You accept the invitation and thank both guests for the conversation. The other guest's frustrations soften a little and they wish you a good next cycle. After a pause they add,"
    );
    nextSectorName = inviterName;
  } else {
    yield text(
      "The other guest says, you must be having second thoughts on your stance on Beings. Come with me to my camp instead, I'm not an ideologue and will not force you to agree with me!"
    );
    const acceptSecond = yield* askYn("Do you accept the guest's invitation?");
    if (acceptSecond) {
      yield text(
        "You accept the invitation and thank both guests for the conversation. The other guest nods saying, of course only you can choose what camp you visit,"
      );
      nextSectorName = inviterName === "Beit" ? "Gimel" : "Beit";
    } else {
      yield text(
        "You say, while I appreciate this dialogue, I am firm in my stance on Beings. Therefore I must accept the other invitation for the next cycle. The other guest nods saying, of course only you can choose what camp you visit,"
      );
      nextSectorName = inviterName;
    }
  }

  yield text("but before you go, can you declare your take on this situation?");
  yield symbol({ symbol: "( ｡ •̀ ``-`` •́ ｡ )", numLines: 1 });

  const worldviewChoice = yield* askMulti("Do you respond with:", [
    { key: "a", label: "This is all made up" },
    { key: "b", label: "I don't care" },
    { key: "c", label: "Other [type your own answer]" },
  ]);

  let worldview: string;
  if (worldviewChoice === "a") worldview = "this is all made up";
  else if (worldviewChoice === "b") worldview = "I don't care";
  else worldview = yield* askFree("Type your response:");

  const newState = expandIdea(state, worldview);

  yield text("The other player thanks you for your response and takes their leave.");
  yield symbol({ symbol: "ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧", numLines: 2 });

  yield text(
    "You leave the party grateful to have some place to go and wondering what just happened and what mysteries await you next cycle."
  );
  yield art(chapterTwoEndArt);

  return {
    toChapter: "chapter03",
    state: newState,
    handoff: { startingSector: nextSectorName },
  };
};
