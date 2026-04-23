import { useState } from "react";
import type { Answer, Prompt } from "../engine/types";

type Props = {
  prompt: Prompt;
  onAnswer: (a: Answer) => void;
  disabled?: boolean;
};

export function Choices({ prompt, onAnswer, disabled = false }: Props) {
  const [freeText, setFreeText] = useState("");

  if (prompt.kind === "yn") {
    return (
      <div className="prompt yn">
        <p className="question" role="status">
          {prompt.question}
        </p>
        <div className="buttons">
          <button disabled={disabled} onClick={() => onAnswer(true)}>
            <span className="opt-key">Y.</span> Yes
          </button>
          <button disabled={disabled} onClick={() => onAnswer(false)}>
            <span className="opt-key">N.</span> No
          </button>
        </div>
      </div>
    );
  }

  if (prompt.kind === "multi") {
    return (
      <div className="prompt multi">
        <p className="question" role="status">
          {prompt.question}
        </p>
        <div className="buttons">
          {prompt.options.map((opt) => (
            <button
              key={opt.key}
              disabled={disabled}
              onClick={() => onAnswer(opt.key)}
            >
              <span className="opt-key">{opt.key}.</span> {opt.label}
            </button>
          ))}
        </div>
      </div>
    );
  }

  const submit = () => {
    const trimmed = freeText.trim();
    if (!trimmed || disabled) return;
    onAnswer(trimmed);
  };

  return (
    <div className="prompt free">
      <p className="question" role="status">
        {prompt.question}
      </p>
      <textarea
        value={freeText}
        onChange={(e) => setFreeText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            e.preventDefault();
            submit();
          }
        }}
        rows={1}
        disabled={disabled}
        autoFocus
      />
      <div className="buttons">
        <button disabled={disabled || !freeText.trim()} onClick={submit}>
          Submit
        </button>
      </div>
    </div>
  );
}
