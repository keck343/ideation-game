import {
  art,
  askYn,
  imageBg,
  imageFg,
  section,
  symbol,
  text,
  typewriter,
  type ChapterFactory,
} from "../engine/helpers";
import { chapterOneArt } from "../data/art";
import { newIdea01, newIdea02, quotes } from "../data/quotes";

export const chapter01: ChapterFactory = function* (state, _handoff) {
  yield imageBg(1);
  yield imageFg(1);
  yield section(1, "Level 1");

  yield art(chapterOneArt);
  yield text("You wake up in an unfamiliar town with no recollection of how you got here.");
  yield text("This world is so many combinations of seemingly disparate things.");
  yield text(
    "You find yourself synthesizing new meanings that make sense to you. The world feels bigger than you ever could have imagined back home."
  );
  yield text("A stranger appears.");
  yield text(
    "As a new comer in a strange land, you override any social anxiety and walk towards them."
  );
  yield text(
    `The stranger turns toward you smiling.\nI'm ${newIdea01}. What's your name?`
  );

  const gaveName = yield* askYn(`Do you want to give ${newIdea01} your name?`);
  if (gaveName) {
    yield text("You freeze, realizing that suddenly you can not recall your name.");
  } else {
    yield text("You shake your head no.");
  }

  yield text(
    `Not to worry, ${newIdea01} says, a lot of new folks here do not yet have names.`
  );
  yield text(
    `A new person runs up to ${newIdea01} saying, I'm running late to worldview club and can not think of a quote to bring.`
  );
  yield text(
    `${newIdea01} introduces the other person as ${newIdea02} to you. They pause, and turn to you and ask you if you have a quote.`
  );

  const quote = quotes[state.playerQuoteKey];
  const gaveQuote = yield* askYn("Do you have a quote to give them?");
  if (gaveQuote) {
    yield text(
      `You smile and say, a quote that resonates with me was once said by ${quote.author}:\n\n"${quote.quote}"`
    );
    yield text(
      `${newIdea02}'s face lights up. I love that quote! They exclaim. Worldview club's membership is currently closed, but we have a dinner party tonight. You should come!`
    );
  } else {
    yield text(
      `${newIdea01} apologies for putting you on the spot. They turn to ${newIdea02} and say: My favorite quote is by ${quote.author}:\n\n"${quote.quote}"`
    );
    yield text("A smile creeps on your face without you realizing it.");
    yield text(
      `${newIdea02} says: It must be a good quote if the new person likes it! I'll use it. Are you going to the after worldview-club dinner party tonight? Everyone is invited!`
    );
  }

  const goParty = yield* askYn("Do you wish to go to the dinner party?");
  if (goParty) {
    yield text(
      `${newIdea02} says, 'Delightful, it starts at 7! See you there!'`
    );
  } else {
    yield text(
      `You reply, 'It's been a long day, and I don't know where I am. I should.....'`
    );
    yield text(
      `Before you can think of where you should be or what you should be doing, ${newIdea01} butts in,`
    );
    yield typewriter(
      `'You look so lost, this will be the thing to lift your spirits! When I first came here, it was important to listen to new ideas and make friends. Plus there will be plenty of people who want to talk about ${quote.author}!`
    );
    yield text(
      `Unable to come up with another excuse and thinking of ${quote.author}, you agree to go for only an hour.`
    );
  }

  yield symbol({ sleepSeconds: 0.25, numLines: 4 });

  return { toChapter: "chapter02", state, handoff: {} };
};
