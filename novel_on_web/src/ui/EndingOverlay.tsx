import type { Beat, PlayAgainPosition } from "../engine/types";
import type { EndingMode } from "../engine/useStory";
import { GrowingSymbol } from "./GrowingSymbol";
import { Typewriter } from "./Typewriter";

type Props = {
  mode: EndingMode | null;
  card: Beat | null;
  cardVersion: number;
  showPlayAgain: boolean;
  playAgainPosition: PlayAgainPosition;
  onReset: () => void;
};

export function EndingOverlay({
  mode,
  card,
  cardVersion,
  showPlayAgain,
  playAgainPosition,
  onReset,
}: Props) {
  if (!mode) return null;
  return (
    <div className={`ending-overlay tone-${mode.tone}`}>
      {card && <EndingCard beat={card} version={cardVersion} />}
      {showPlayAgain && (
        <div className={`ending-play-again pos-${playAgainPosition}`}>
          <button onClick={onReset}>Play again</button>
        </div>
      )}
    </div>
  );
}

function EndingCard({ beat, version }: { beat: Beat; version: number }) {
  switch (beat.kind) {
    case "epitaph": {
      const variant = beat.variant ?? "default";
      return (
        <div
          key={version}
          className={`ending-card epitaph variant-${variant}`}
        >
          {beat.text}
        </div>
      );
    }
    case "credits":
      return (
        <div key={version} className="ending-card credits">
          {beat.lines.map((line, i) => (
            <div key={i} className={line ? "line" : "line spacer"}>
              {line || "\u00A0"}
            </div>
          ))}
        </div>
      );
    case "art":
      return (
        <pre key={version} className="ending-card art">
          {beat.text}
        </pre>
      );
    case "text":
      return (
        <div
          key={version}
          className="ending-card epitaph variant-default"
        >
          {beat.text}
        </div>
      );
    case "typewriter":
      return (
        <div
          key={version}
          className="ending-card epitaph variant-default typewriter"
        >
          <Typewriter text={beat.text} cps={beat.cps} />
        </div>
      );
    case "symbol":
      return (
        <div key={version} className="ending-card symbol">
          <GrowingSymbol
            symbol={beat.symbol ?? "*"}
            numLines={beat.numLines ?? 7}
            sleepSeconds={beat.sleepSeconds ?? 0.5}
          />
        </div>
      );
    default:
      return null;
  }
}
