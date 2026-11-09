import { useContext, useEffect, useMemo, useRef, useState } from "react";
import { SkipContext } from "./SkipContext";
import { RichText } from "./RichText";
import { parseInline, plainLength } from "./inlineMarkup";

type Props = {
  text: string;
  cps?: number;
  onDone?: () => void;
  immediate?: boolean;
  italic?: boolean;
};

export function Typewriter({ text, cps = 60, onDone, immediate, italic }: Props) {
  const total = useMemo(() => plainLength(parseInline(text)), [text]);
  const [shown, setShown] = useState(immediate ? total : 0);
  const [skipped, setSkipped] = useState(immediate ?? false);
  const skipTick = useContext(SkipContext);
  const mountTickRef = useRef(skipTick);

  useEffect(() => {
    if (skipTick === mountTickRef.current) return;
    setSkipped(true);
  }, [skipTick]);

  useEffect(() => {
    if (skipped) {
      setShown(total);
      onDone?.();
      return;
    }
    if (shown >= total) {
      onDone?.();
      return;
    }
    const interval = 1000 / cps;
    const id = setTimeout(() => setShown((s) => s + 1), interval);
    return () => clearTimeout(id);
  }, [shown, total, cps, skipped, onDone]);

  return (
    <p className={`beat typewriter${italic ? " italic" : ""}`}>
      <RichText text={text} shown={shown} />
      {shown < total && <span className="caret">▌</span>}
    </p>
  );
}
