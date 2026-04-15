import type { Beat } from "../engine/types";
import { Typewriter } from "./Typewriter";
import { GrowingSymbol } from "./GrowingSymbol";

export function BeatDisplay({ beat }: { beat: Beat }) {
  switch (beat.kind) {
    case "text":
      return <p className="beat text">{beat.text}</p>;
    case "art":
      return <pre className="beat ascii-art">{beat.text}</pre>;
    case "typewriter":
      return <Typewriter text={beat.text} cps={beat.cps} />;
    case "symbol":
      return (
        <GrowingSymbol
          symbol={beat.symbol ?? "*"}
          numLines={beat.numLines ?? 7}
          sleepSeconds={beat.sleepSeconds ?? 0.5}
        />
      );
    case "section":
      return <h2 className="beat section">{beat.title}</h2>;
    case "pause":
      return <div className="beat pause" />;
    case "image":
    case "endingMode":
    case "epitaph":
    case "credits":
    case "playAgain":
      // consumed by the engine or rendered by EndingOverlay; never appears in the terminal log
      return null;
  }
}
