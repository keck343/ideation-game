import { useContext, useEffect, useState } from "react";
import { SkipContext } from "./SkipContext";

type Props = { text: string; cps?: number; onDone?: () => void };

export function Typewriter({ text, cps = 60, onDone }: Props) {
  const [shown, setShown] = useState(0);
  const [skipped, setSkipped] = useState(false);
  const skipTick = useContext(SkipContext);

  useEffect(() => {
    if (skipTick > 0) setSkipped(true);
  }, [skipTick]);

  useEffect(() => {
    if (skipped) {
      setShown(text.length);
      onDone?.();
      return;
    }
    if (shown >= text.length) {
      onDone?.();
      return;
    }
    const interval = 1000 / cps;
    const id = setTimeout(() => setShown((s) => s + 1), interval);
    return () => clearTimeout(id);
  }, [shown, text, cps, skipped, onDone]);

  return (
    <p className="beat typewriter">
      {text.slice(0, shown)}
      {shown < text.length && <span className="caret">▌</span>}
    </p>
  );
}
