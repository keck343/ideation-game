export type InlineSegment = { text: string; italic: boolean; bold: boolean };

const isWordChar = (c: string | undefined) =>
  c !== undefined && /[\p{L}\p{N}]/u.test(c);
const isSpace = (c: string | undefined) => c === undefined || /\s/.test(c);

export function parseInline(source: string): InlineSegment[] {
  const segments: InlineSegment[] = [];
  let buffer = "";
  let italic = false;
  let bold = false;

  const flush = () => {
    if (buffer) segments.push({ text: buffer, italic, bold });
    buffer = "";
  };

  const canOpen = (i: number, len: number) =>
    !isWordChar(source[i - 1]) && !isSpace(source[i + len]);
  const canClose = (i: number, len: number) =>
    !isSpace(source[i - 1]) && !isWordChar(source[i + len]);

  const hasCloser = (marker: string, from: number) => {
    let j = source.indexOf(marker, from);
    while (j !== -1) {
      if (canClose(j, marker.length)) return true;
      j = source.indexOf(marker, j + 1);
    }
    return false;
  };

  let i = 0;
  while (i < source.length) {
    const ch = source[i];
    const next = source[i + 1];

    if (ch === "\\" && (next === "_" || next === "*")) {
      buffer += next;
      i += 2;
      continue;
    }

    const marker = source.startsWith("**", i) ? "**" : ch === "_" ? "_" : null;
    if (marker) {
      const isBold = marker === "**";
      const active = isBold ? bold : italic;
      if (active && canClose(i, marker.length)) {
        flush();
        if (isBold) bold = false;
        else italic = false;
        i += marker.length;
        continue;
      }
      if (
        !active &&
        canOpen(i, marker.length) &&
        hasCloser(marker, i + marker.length)
      ) {
        flush();
        if (isBold) bold = true;
        else italic = true;
        i += marker.length;
        continue;
      }
    }

    buffer += ch;
    i++;
  }
  flush();
  return segments;
}

export function plainLength(segments: InlineSegment[]): number {
  return segments.reduce((n, s) => n + s.text.length, 0);
}
