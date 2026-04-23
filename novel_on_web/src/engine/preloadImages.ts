const BASE = `${import.meta.env.BASE_URL}images`;

const IMAGES: string[] = [
  ...[0, 3, 4, 5, 6, 7, 8].map((n) => `${BASE}/back_${n}.jpg`),
  ...[1, 2, 3, 4, 5, 6, 7].map((n) => `${BASE}/level_${n}.webp`),
  ...[0, 1].map((n) => `${BASE}/end_${n}.webp`),
];

export function preloadImages(): void {
  const run = () => {
    for (const src of IMAGES) {
      const img = new Image();
      img.src = src;
    }
  };
  if (typeof window === "undefined") return;
  const ric = (window as Window & {
    requestIdleCallback?: (cb: () => void) => number;
  }).requestIdleCallback;
  if (ric) ric(run);
  else window.setTimeout(run, 200);
}
