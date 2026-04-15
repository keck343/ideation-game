import {
  art,
  credits,
  endingMode,
  epitaph,
  imageBg,
  imageEnd,
  imageFg,
  pause,
  playAgain,
  symbol,
  typewriter,
  type ChapterFactory,
} from "../engine/helpers";
import { heartOfZeros } from "../data/art";
import { campByName, skalismoCamp } from "../data/camps";

type Handoff = {
  finalCampName: string;
  finalNumRoundsInCamp: number;
};

export const ending: ChapterFactory = function* (state, handoffIn) {
  const { finalCampName, finalNumRoundsInCamp } = handoffIn as Handoff;
  const endCamp = campByName(finalCampName);

  const worldSurvived =
    finalNumRoundsInCamp > 0 && endCamp?.knownName === skalismoCamp.knownName;

  yield imageBg(8);
  yield imageFg(null);
  yield pause(0.6);

  const tone: "cold" | "neutral" | "warm" = worldSurvived ? "warm" : "cold";
  yield endingMode({ titleSuffix: "— The End", tone });
  yield pause(2.2);

  if (!worldSurvived) {
    let playerWins = false;

    if (state.desiredEndStateKey === "a") {
      yield epitaph({ text: "You did get to finish your novel.", hold: 3400 });
      playerWins = true;

      yield typewriter(
        "As you relish in the prose, the last being perished and like the rest of the embodied, you disappeared into the void.",
        55,
      );
      yield pause(1.4);

      yield symbol({ symbol: "+=={:::::::::::::::::>", numLines: 3 });
      yield pause(1.8);

      yield epitaph({
        text: "You achieved your goal, but you did not survive much longer to enjoy your victory because no one did.",
        hold: 5600,
      });
      yield pause(2.2);
    }

    if (
      endCamp &&
      endCamp.endStateKey === state.desiredEndStateKey &&
      finalNumRoundsInCamp > 0 &&
      !["d", "c"].includes(state.desiredEndStateKey)
    ) {
      playerWins = true;
    }

    if (playerWins) {
      yield imageEnd(1);
      yield pause(0.6);
      yield symbol({ symbol: "+=={:::::::::::::::::>", numLines: 3 });
      yield pause(1.6);

      yield epitaph({
        text: "Unlike the real world, there is a diagram for how this world works.\nSince you did achieve your goal,\nGive the passcode 'all\u00A0caffeine'\nto the bartender to get the diagram.",
        hold: 7400,
      });
      yield pause(1.2);

      yield epitaph({
        text: "Maybe you will want to play again with this new knowledge.",
        hold: 4200,
      });
      yield pause(1.4);

      yield playAgain();
    } else {
      yield imageEnd(0);
      yield pause(1.2);

      yield symbol({ symbol: "+=={:::::::::::::::::>", numLines: 3 });
      yield pause(1.6);

      yield epitaph({
        text: "How the world works will remain a mystery,\nbut unlike real life,\nyou can choose to play this game again.",
        hold: 5200,
      });
      yield pause(1.4);

      yield playAgain({ position: "bottom" });
    }
  } else {
    let playerWins = false;
    if (["d", "c"].includes(state.desiredEndStateKey)) {
      playerWins = true;
    }

    yield imageEnd(1);
    yield pause(1);

    yield epitaph({
      text: "In the end, your camp stopped the death of the embodied and Beings.\nWhile the world could never be the same again,\nAttention flows through out all the camps.",
      hold: 5400,
    });
    yield pause(1);

    yield symbol({ symbol: "√♥-√v--√♥-√v–", numLines: 3 });
    yield pause(1.6);

    if (state.desiredEndStateKey === "b") {
      yield epitaph({
        text: "Your new found camp survived and allowed other camps to survive.\nThis came voice grew but did not dominate.",
        hold: 5200,
      });
      yield pause(1.4);
    } else if (["e", "f"].includes(state.desiredEndStateKey)) {
      yield epitaph({
        text: "Your attempts at fame however were fleeting.\nYour fellow camp members were fed up with your ego, and no one will talk to you.",
        hold: 5800,
      });
      yield pause(1.4);
    } else if (playerWins) {
      yield epitaph({ text: "You sigh in relief.", hold: 2800 });
      yield pause(0.6);
      yield epitaph({
        text: "You achieved your goal and the world goes on.",
        hold: 4200,
      });
      yield pause(1.2);
    }

    yield art(heartOfZeros);
    yield pause(3);

    yield epitaph({
      text: "Unlike the real world, there is a diagram for how this world works.\nSince the world survived,\nGive the passcode 'all\u00A0caffeine'\nto the bartender to get the diagram.",
      hold: 8400,
    });
    yield pause(1.6);

    yield credits({
      lines: ["Disambiguation", "by Quinn Keck"],
      hold: 8000,
    });
    yield pause(1.6);

    yield imageEnd(null);
    yield pause(4);

    yield playAgain();
  }

  return { toChapter: "ending", state, handoff: { done: true } };
};
