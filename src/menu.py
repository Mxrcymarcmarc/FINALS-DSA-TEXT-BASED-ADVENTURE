from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.align import Align
from rich import print
from rich.columns import Columns
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

MAX_ENERGY = 10

state = {
    "day": 1,
    "energy": MAX_ENERGY,
    "choices" : []
}

def titleMenu():
    console = Console()
    layout = Layout(name="Root")
    
    layout.split_column(
        Layout(name="Top", size=4),
        Layout(name="Middle", size=20),
        Layout(name="Bottom", size=10)
    )
    
    layout["Top"].split_row(
        Layout(name="Bar", ratio=3),
        Layout(name="Day", ratio=1)
    )
    
    layout["Middle"].split_row(
        Layout(name="Screen", ratio=3),
        Layout(name="List", ratio=1)
    )
    
    layout["Bottom"].split_row(
        Layout(name="Choices", ratio=3),
        Layout(name="Controls", ratio=1)
    )
    
    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
    )
    task = progress.add_task("", total=MAX_ENERGY)
    progress.update(task, completed=state["energy"])
    
    layout["Bar"].update(Panel(progress, title="Energy"))
    layout["Day"].update(Panel(f"Day {state['day']}", title="Current Day"))
    
    layout["Screen"].update(Panel("tite", title="Main Screen", border_style="white"))

    print(layout)
    
def energyChange(choice):
    if choice == "1":
        effect = -1
        label = "Conformed"
    else:
        effect = +1
        label = "Created"

    state["energy"] = max(0, min(MAX_ENERGY, state["energy"] + effect))

    state["choices"].append({
        "day": state["day"],
        "choice": label,
        "effect": effect
    })

    state["day"] += 1