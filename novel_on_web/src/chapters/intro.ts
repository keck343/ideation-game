import {
  addSector,
  art,
  askMulti,
  imageBg,
  imageEnd,
  imageFg,
  section,
  symbol,
  text,
  type ChapterFactory,
} from "../engine/helpers";
import { welcomeArt } from "../data/art";
import { quotes } from "../data/quotes";
import { initialPlayerState } from "../engine/types";

export const intro: ChapterFactory = function* (_state, _handoff) {
  yield imageBg(0);
  yield imageFg(null);
  yield imageEnd(null);
  yield section(0, "Disambiguation");
  yield art(welcomeArt);
  yield text("Welcome to Disambiguation.");
  yield text(
    "The blank canvas of creation is heaven or hell depending on your perspective.",
  );
  yield text("Pick the quote that most resonates with you:");

  const quoteKey = yield* askMulti(
    "Pick the quote that most resonates with you",
    Object.entries(quotes).map(([key, q]) => ({
      key,
      label: `From ${q.author}: "${q.quote}"`,
    })),
    { noRecap: true },
  );

  const chosen = quotes[quoteKey];
  if (chosen) {
    yield text(`From ${chosen.author}: '${chosen.quote}'`);
  }

  yield symbol({ sleepSeconds: 0.5 });

  const fresh = initialPlayerState(quoteKey);
  // bias sectors list as empty to start; chapter 1 will seed things
  return {
    toChapter: "chapter01",
    state: addSector(fresh, ""), // no-op, just for parity
    handoff: {},
  };
};
