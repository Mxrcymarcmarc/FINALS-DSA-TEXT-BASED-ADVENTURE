from rich.panel import Panel
from rich.live import Live
from rich.console import Console
import time

console = Console()

def printScene(text, delay=0.02):
    displayed = ""  # what has been printed so far

    with Live(console=console, refresh_per_second=20, screen=False) as live:
        for char in text:
            displayed += char
            live.update(Panel(displayed, title="Main Screen", box=None))
            time.sleep(delay)

# Example usage
story_text = """Nolan walks past cafés.
Past offices.
Past construction fences wrapped in advertisements for futures he isn't part of."""
printScene(story_text)
