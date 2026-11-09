import { Fragment, useMemo, type ReactNode } from "react";
import { parseInline } from "./inlineMarkup";

type Props = { text: string; shown?: number };

export function RichText({ text, shown }: Props) {
  const segments = useMemo(() => parseInline(text), [text]);
  let remaining = shown ?? Infinity;
  const nodes: ReactNode[] = [];

  for (let i = 0; i < segments.length && remaining > 0; i++) {
    const seg = segments[i];
    const visible =
      seg.text.length <= remaining ? seg.text : seg.text.slice(0, remaining);
    remaining -= visible.length;
    let node: ReactNode = visible;
    if (seg.bold) node = <strong>{node}</strong>;
    if (seg.italic) node = <em>{node}</em>;
    nodes.push(<Fragment key={i}>{node}</Fragment>);
  }

  return <>{nodes}</>;
}
