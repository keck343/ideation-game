import { Component, type ReactNode } from "react";

type Props = { children: ReactNode };
type State = { error: Error | null };

export class ErrorBoundary extends Component<Props, State> {
  state: State = { error: null };

  static getDerivedStateFromError(error: Error): State {
    return { error };
  }

  componentDidCatch(error: Error, info: { componentStack?: string | null }) {
    console.error("Disambiguation crashed:", error, info);
  }

  handleReload = () => {
    window.location.reload();
  };

  render() {
    if (!this.state.error) return this.props.children;
    return (
      <div className="error-screen" role="alert">
        <h1>The terminal has gone dark.</h1>
        <p>Something broke while rendering the story.</p>
        <pre>{this.state.error.message}</pre>
        <button onClick={this.handleReload}>Reload</button>
      </div>
    );
  }
}
