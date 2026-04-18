type Props = {
  onContinue: () => void;
  onNewGame: () => void;
};

export function ResumePrompt({ onContinue, onNewGame }: Props) {
  return (
    <div className="resume-prompt">
      <p className="resume-text">You have a saved game.</p>
      <div className="resume-actions">
        <button onClick={onContinue}>Continue</button>
        <button onClick={onNewGame}>Start Anew</button>
      </div>
    </div>
  );
}
