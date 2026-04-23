import { useContext, useEffect, useRef, useState } from "react";
import { SkipContext } from "./SkipContext";

type Props = { text: string; cps?: number; onDone?: () => void; immediate?: boolean };

export function Typewriter({ text, cps = 60, onDone, immediate }: Props) {
  const [shown, setShown] = useState(immediate ? text.length : 0);
  const [skipped, setSkipped] = useState(immediate ?? false);
  const skipTick = useContext(SkipContext);
  const mountTickRef = useRef(skipTick);

  useEffect(() => {
    if (skipTick === mountTickRef.current) return;
    setSkipped(true);
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
