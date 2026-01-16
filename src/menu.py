from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.console import Console, Group
from rich.align import Align
from rich import print
from rich.columns import Columns
from rich.live import Live
from rich.progress import Progress, BarColumn, TextColumn
import story
import msvcrt
import os
import sys
import time

MIN_CD = 0
MAX_CD = 100

state = {
    "day": 1,
    "creative_drive": MAX_CD,
    "flags": set(),
    "history": [],
    "choices": ["A. bjhcbajbajbc", "B. vxhxvhxajb"],
    "last_cd_change": None
}

sceneState = {
    "id": 0,
    "title": "",
    "text": "",
    "choices": ""
}

theArchi = r"""
    ████████╗ ██╗   ██╗ ██████╗    ██████╗  ██████╗    ██████╗ ██╗   ██╗ ████████╗ ████████╗ ██████╗  ██████╗ ████████╗
    ╚══██╔══╝ ██║   ██║ ██╔═══╝   ██╔═══██╗ ██╔══██╗  ██╔════╝ ██║   ██║ ╚══██╔══╝ ╚══██╔══╝ ██╔═══╝ ██╔════╝ ╚══██╔══╝
       ██║    ████████║ █████║    ████████║ ██████╔╝  ██║      ████████║    ██║       ██║    █████║  ██║         ██║ 
       ██║    ██╔═══██║ ██╔══╝    ██║   ██║ ██╔══██║  ██║      ██╔═══██║    ██║       ██║    ██╔══╝  ██║         ██║
       ██║    ██║   ██║ ██████║   ██║   ██║ ██║   ██╗ ╚██████╗ ██║   ██║ ████████╗    ██║    ██████║ ╚██████╗    ██║
       ╚═╝    ╚═╝   ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═╝   ╚═╝  ╚═════╝ ╚═╝   ╚═╝ ╚═══════╝    ╚═╝    ╚═════╝  ╚═════╝    ╚═╝
"""
gameOver = r"""
     ██████╗   ██████╗  ███╗   ███╗ ███████╗    ██████╗  ███╗   ███╗ ███████╗ ██████╗  
    ██╔════╝  ██╔═══██╗ ████╗ ████║ ██╔════╝   ██╔═══██╗  ██║   ██╔╝ ██╔════╝ ██╔══██╗ 
    ██║       ████████║ ██╔████╔██║ █████╗     ██║   ██║   ██╗ ██╔╝  █████╗   ██████╔╝ 
    ██║   ██╗ ██║   ██║ ██║╚██╔╝██║ ██╔══╝     ██║   ██║    ████╔╝   ██╔══╝   ██╔══██║ 
    ╚███████║ ██║   ██║ ██║ ╚═╝ ██║ ███████╗   ╚██████╔╝    ╚██╔╝    ███████╗ ██║   ██╗
     ╚══════╝ ╚═╝   ╚═╝ ╚═╝     ╚═╝ ╚══════╝    ╚═════╝      ╚═╝     ╚══════╝ ╚═╝   ╚═╝
"""
theEnd = r"""
    ████████╗ ██╗   ██╗ ██████╗   ██████╗ ███╗   ██╗ ███████╗ 
    ╚══██╔══╝ ██║   ██║ ██╔═══╝   ██╔═══╝ ████╗  ██║ ██╔═══██╗
       ██║    ████████║ █████║    █████║  ██╔██╗ ██║ ██║   ██║
       ██║    ██╔═══██║ ██╔══╝    ██╔══╝  ██║╚██╗██║ ██║   ██║
       ██║    ██║   ██║ ██████║   ██████║ ██║ ╚████║ ███████╔╝
       ╚═╝    ╚═╝   ╚═╝ ╚═════╝   ╚═════╝ ╚═╝  ╚═══╝ ╚══════╝ 
"""

def stateUpdater(scene):
    sceneState["choice_keys"] = list(scene["choices"].keys())
    sceneState["id"] = scene["id"]
    sceneState["title"] = scene["title"]
    sceneState["text"] = scene["text"]
    sceneState["choices"] = [
        choice["text"]
        for choice in scene["choices"].values()
    ]
    return scene

def clear():
    os.system("cls")

def keys():
    keyPress = r"""
         Navigation Keys
         
           ⇅     Move Selection
         Enter   Select
          Esc    Exit
    """
    return Panel(keyPress, box=box.MINIMAL)

def mainScreen():
    console = Console()
    layout = Layout()
    
    clear()

    menuTexts = ["New Game", "Exit Game"]
    selected = 0

    # Setup layout
    layout.split_column(
        Layout(name="Top", size=11),
        Layout(name="Middle", size=8)
    )
    layout["Middle"].split_row(
        Layout(name="Navigation", ratio=1),
        Layout(name="Menu", ratio=2),
        Layout(name="Extra", ratio=1)
        
    )

    def build_menu():
        menuContent = ""
        for i, text in enumerate(menuTexts):
            if i == selected:
                menuContent += f"[bold #51AE7D]> {text} <[/bold #51AE7D]\n"
            else:
                menuContent += f"  {text} \n"

        return Panel(
            Align.center(Text.from_markup(menuContent), vertical="middle"),
            title="Menu",
            padding=(1, 2),
            box=box.MINIMAL
        )
    extra = Panel(" ", box=box.MINIMAL) 
    header = Panel(
        Align.center(
            Group(
                Align(Text(theArchi, style="bold #AE5182")),
                Align.center(Text("Made By GROUP 4", justify="center", style="bold #AE5182")))),
        border_style="#5aa580",
        box=box.MINIMAL)  

    # Initial update
    layout["Top"].update(header)
    layout["Navigation"].update(keys())
    layout["Menu"].update(build_menu())
    layout["Extra"].update(extra)

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
    
    layout.split_column(
        Layout(name="Top", size=3),
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
    
    def cdPanel():
        progress = Progress(
        TextColumn("[bold #F0B01D]{task.total}[/bold #F0B01D]", style="yellow"),
        BarColumn(
            bar_width=50,
            style="bright_black",
            finished_style="#F0B01D"
        ),
        expand=True)
    
        task = progress.add_task("", total=MAX_CD)
        progress.update(task, completed=50)
        
        delta = state.get("last_cd_change", 0)
        
        if delta is None:
            delta_text = Text("")
        elif delta > 0:
            delta_text = Text(f"+{delta}", style="bold green")
        elif delta < 0:
            delta_text = Text(f"-{delta}", style="bold red")
        else: 
            delta_text = Text(f"{delta}", style="bold white")
            
        return Panel(
            Columns([progress, delta_text], align="left"),
            box=box.MINIMAL,
        )
        
    def historyPanel():
        if not state["history"]:
            return Panel("Choices are stored here.", title="History")
        
        lines=[]
        for entry in state["history"][-6:]:
            cd = entry["cd_change"]
            color = "green" if cd>0 else "red" if cd<0 else "white"
            sign = f"+{cd}" if cd>0 else str(cd)
            
            lines.append(
                Text(f"Scene {entry['scene_id']} | {entry['choice']} {sign}", style = color)
            )
        
        return Panel(
            Align.left(Text("\n").join(lines)),
            title="History",
            border_style="#AE5182"
        )
    
    def buildChoices():
        choicesContent = ""
        for i, text in enumerate(state["choices"]):
            if i == selected:
                choicesContent += f"[bold #51AE7D]> {text} <[/bold #51AE7D]\n"
            else:
                choicesContent += f"  {text}\n"
        return Panel(choicesContent, 
                     title="Choices", 
                     border_style="#AE5182",
                     padding=1)  
    
    layout["Bar"].update(cdPanel())
    
    day_text = Text(
        f"DAY {state['day']}",
        justify="center",
        style="bold #AE5182"
    )

    layout["Day"].update(
        Panel(
            Align.center(day_text, vertical="middle", style="#AE5182"),
            box=box.MINIMAL)
    )
    
    layout["List"].update(historyPanel())
    
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
    
def applyChoice(state, scene, choice_key):
    choice = scene["choices"][choice_key]

    cd_before = state["creative_drive"]

    state["creative_drive"] += choice["cd_change"]
    state["creative_drive"] = max(MIN_CD, min(MAX_CD, state["creative_drive"]))
    
    cd_after = state["creative_drive"]

    state["flags"].add(choice["flag"])

    state["history"].append(
        {
            "scene_id": scene["id"],
            "choice": choice_key,
            "cd_change": choice["cd_change"]
        }
    )
    
    state["last_cd_change"] = cd_after - cd_before

    return choice["bridge"]

def endScreen():
    console = Console()
    layout = Layout()
    
    clear()
    
    layout.split_column(
        Layout(name="Top", size=11),
        Layout(name="Middle", size=8))
    
    header = Panel(
        Align.center(
            Group(
                Align(Text(theEnd, style="bold #AE5182")),
                Align.center(Text("Ending ??: wowow", justify="center", style="bold #51AE7D")))),
        border_style="#5aa580",
        box=box.MINIMAL) 
    
    layout["Top"].update(header)
    
    endPrompt = header = Panel(
        Align.center(Text("Press any key to go back to menu.")),
        box=box.MINIMAL)
    
    layout["Middle"].update(endPrompt)
    
    print(layout)
    key = msvcrt.getch()
    mainScreen()