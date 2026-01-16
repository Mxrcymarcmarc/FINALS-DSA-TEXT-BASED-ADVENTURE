from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.console import Console
from rich.align import Align
from rich import print
from rich.columns import Columns
from rich.live import Live
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
import msvcrt
import os
import sys
import time

def clear():
    os.system("cls")

MAX_ENERGY = 100
state = {
    "day": 1,
    "energy": MAX_ENERGY,
    "choices": ["a", "b"]
}

def keys():
    keyPress = r"""
       ⇅     Move Selection
     Enter   Select
      Esc    Exit
    """
    return Panel(keyPress, title="Navigation Keys", border_style="blue")

def mainScreen():
    console = Console()
    layout = Layout()

    menuTexts = ["New Game", "Exit Game"]
    selected = 0

    # Setup layout
    layout.split_column(
        Layout(name="Top", size=15),
        Layout(name="Middle", size=8)
    )
    layout["Middle"].split_row(
        Layout(name="Navigation", ratio=1),
        Layout(name="Menu", ratio=2)
    )

    def build_menu():
        menuContent = ""
        for i, text in enumerate(menuTexts):
            if i == selected:
                menuContent += f"[bold #E1B34B]> {text} <[/bold #E1B34B]\n"
            else:
                menuContent += f"  {text}\n"
        return Panel(menuContent, 
                     title="Pokemon Menu", 
                     border_style="blue",
                     padding=1)

    # Initial update
    layout["Navigation"].update(keys())
    layout["Menu"].update(build_menu())

    clear()
    with Live(layout, console=console, refresh_per_second=20, screen=True):
        while True:
            key = msvcrt.getch()

            # Arrow keys (special codes)
            if key in (b'\xe0', b'\x00'):
                key = msvcrt.getch()
                if key == b'P':  # DOWN
                    selected = (selected + 1) % len(menuTexts)
                elif key == b'H':  # UP
                    selected = (selected - 1) % len(menuTexts)

                layout["Menu"].update(build_menu())

            # Enter key
            elif key == b'\r':
                if selected == len(menuTexts) - 1:  # Exit option
                    exit()
                else:
                    return selected # New Game chosen

            # Esc key
            elif key == b'\x1b':
                exit()

def storyScreen():
    console = Console()
    layout = Layout()
    
    selected = 0
    
    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"))
    
    task = progress.add_task("", total=MAX_ENERGY)
    
    layout.split_column(
        Layout(name="Top", size=4),
        Layout(name="Middle", size=20),
        Layout(name="Bottom", size=10))
    
    layout["Top"].split_row(
        Layout(name="Bar", ratio=3),
        Layout(name="Day", ratio=1))
    
    layout["Middle"].split_row(
        Layout(name="Screen", ratio=3),
        Layout(name="List", ratio=1))
    
    layout["Bottom"].split_row(
        Layout(name="Choices", ratio=3),
        Layout(name="Controls", ratio=1))
    
    progress.update(task, completed=state["energy"])
    
    # def printScene(text, delay=0.02):
    #     displayed = ""  # what has been printed so far

    #     with Live(console=console, refresh_per_second=20, screen=False) as live:
    #         for char in text:
    #             displayed += char
    #             live.update(Panel(displayed, title="Main Screen", box=None))
    #             time.sleep(delay)

    # # Example usage
    # story_text = """Nolan walks past cafés.
    # Past offices.
    # Past construction fences wrapped in advertisements for futures he isn't part of."""
    # printScene(story_text)
    
    def buildChoices():
        choicesContent = ""
        for i, text in enumerate(state["choices"]):
            if i == selected:
                choicesContent += f"[bold #E1B34B]> {text} <[/bold #E1B34B]\n"
            else:
                choicesContent += f"  {text}\n"
        return Panel(choicesContent, 
                     title="Choices", 
                     border_style="blue",
                     padding=1)  
    
    layout["Bar"].update(
        Panel(
            progress,
            title="Energy",
            box=box.MINIMAL,
        )
    )
    
    layout["Day"].update(Panel(
        f"Day {state["day"]}",
        title="Current Day",
        box=box.MINIMAL))
    
    # layout["Screen"].update(printScene())
    layout["Choices"].update(buildChoices())
    layout["Controls"].update(keys())
    
    clear()
    with Live(layout, console=console, refresh_per_second=20, screen=True):
        while True:
            key = msvcrt.getch()

            # Arrow keys (special codes)
            if key in (b'\xe0', b'\x00'):
                key = msvcrt.getch()
                if key == b'P':  # DOWN
                    selected = (selected + 1) % len(state["choices"])
                elif key == b'H':  # UP
                    selected = (selected - 1) % len(state["choices"])

                layout["Choices"].update(buildChoices())

            # Enter key
            elif key == b'\r':
                if selected == len(state["choices"]) - 1: 
                    pass # B option
                else:
                    pass # A option

            # Esc key
            elif key == b'\x1b':
                exit()
    
def energyChange(choice):
    if choice == "1":
        effect = -1
        label = "Conformed"
    else:
        effect = +1
        label = "Created"

    state["energy"] = max(0, min(MAX_ENERGY, state["energy"] + effect))

    state["choices"].append({
        "day": state['day'],
        "choice": label,
        "effect": effect
    })

    state["day"] += 1