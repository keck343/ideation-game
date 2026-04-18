import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { createHash } from "node:crypto";
import { readdirSync, readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));

function storyContentHash(): string {
  const hash = createHash("sha256");
  for (const dir of ["src/chapters", "src/data"]) {
    const full = resolve(root, dir);
    for (const file of readdirSync(full).sort()) {
      hash.update(readFileSync(resolve(full, file)));
    }
  }
  return hash.digest("hex").slice(0, 12);
}

export default defineConfig({
  base: "/ideation-game/",
  plugins: [react()],
  define: {
    __STORY_VERSION__: JSON.stringify(storyContentHash()),
  },
});
