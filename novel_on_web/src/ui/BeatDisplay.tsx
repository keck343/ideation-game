import type { Beat } from "../engine/types";
import { Typewriter } from "./Typewriter";
import { GrowingSymbol } from "./GrowingSymbol";

export function BeatDisplay({
  beat,
  restored,
}: {
  beat: Beat;
  restored?: boolean;
}) {
  switch (beat.kind) {
    case "text":
      return (
        <p className={`beat text${beat.italic ? " italic" : ""}`}>
          {beat.text}
        </p>
      );
    case "art":
      return <pre className="beat ascii-art">{beat.text}</pre>;
    case "typewriter":
      return (
        <Typewriter text={beat.text} cps={beat.cps} immediate={restored} />
      );
    case "symbol":
      return (
        <GrowingSymbol
          symbol={beat.symbol ?? "*"}
          numLines={beat.numLines ?? 7}
          sleepSeconds={beat.sleepSeconds ?? 0.5}
          immediate={restored}
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
      return null;
  }
}
