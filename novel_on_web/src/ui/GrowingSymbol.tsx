import { useContext, useEffect, useRef, useState } from "react";
import { SkipContext } from "./SkipContext";

type Props = {
  symbol: string;
  numLines: number;
  sleepSeconds: number;
};

function fibLine(symbol: string, index: number): string {
  let a = 1;
  let b = 1;
  for (let i = 0; i < index; i++) {
    const n = a + b;
    a = b;
    b = n;
  }
  return symbol.repeat(b);
}

export function GrowingSymbol({ symbol, numLines, sleepSeconds }: Props) {
  const [lines, setLines] = useState<string[]>([symbol]);
  const skipTick = useContext(SkipContext);
  const mountTickRef = useRef(skipTick);

  useEffect(() => {
    if (skipTick === mountTickRef.current) return;
    setLines((prev) => {
      if (prev.length >= numLines) return prev;
      const rest: string[] = [];
      for (let i = prev.length; i < numLines; i++) {
        rest.push(fibLine(symbol, i));
      }
      return [...prev, ...rest];
    });
  }, [skipTick, numLines, symbol]);

  useEffect(() => {
    if (lines.length >= numLines) return;
    const id = setTimeout(() => {
      setLines((prev) => [...prev, fibLine(symbol, prev.length)]);
    }, sleepSeconds * 1000);
    return () => clearTimeout(id);
  }, [lines, numLines, sleepSeconds, symbol]);

  return <pre className="beat symbol-transition">{lines.join("\n")}</pre>;
}
