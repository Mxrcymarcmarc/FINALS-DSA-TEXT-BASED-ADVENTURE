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
    "last_cd_change": None
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

def clear():
    os.system("cls")

def resetGame():
    state["day"] = 1
    state["scene_id"] = 1
    state["creative_drive"] = MAX_CD
    state["flags"] = set()
    state["history"] = []
    state["last_cd_change"] = None

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

def getDayData():
    """
    Robust day lookup: builds attribute name from state['day'].
    Tries both naming patterns used in story.py: DAY_2_1 and DAY2_1.
    Returns None if attribute missing or not a mapping with 'scenes'.
    """
    d = state.get("day")
    if d is None:
        return None

    # normalize numeric to "2_1" form
    s = str(d).replace('.', '_')
    # remove trailing _0 for exact integers represented as floats like '2_0'
    if s.endswith('_0'):
        s = s[:-2]

    # try both naming conventions
    for attr in (f"DAY_{s}", f"DAY{s}"):
        day_data = getattr(story, attr, None)
        if isinstance(day_data, dict):
            return day_data

    return None

def getCurrentScene():
    day_data = getDayData()
    if not day_data:
        return None
   
    scenes = day_data.get("scenes", [])
    for scene in scenes:
        if scene.get("id") == state["scene_id"]:
            return scene
       
    return None


def dayTransition():
    current_day = state["day"]
    flags = state["flags"]
   
    if current_day == 1:
        state["scene_id"] = 1
       
        authentic_count = sum(1 for f in ["values_authenticity","resists_pressure", "reconnects_with_self"] if f in flags)
        conflicted_count = sum(1 for f in ["conflicted_path", "seeks_validation", "leans_to_compliance"] if f in flags)
        detached_count = sum(1 for f in ["suppresses_identity", "emotional_avoidance"] if f in flags)
       
        if authentic_count >= 2:
            state["day"] = 2.1
        elif conflicted_count >= 2:
            state["day"] = 2.2
        elif detached_count >= 2:
            state["day"] = 2.3
        else:
            state["day"] = 2.2


        return True
   
    elif int(current_day) == 2:
        state["scene_id"] = 1
        state["day"] = current_day + 1.0
        return True
   
    elif int(current_day) == 3:
        state["scene_id"] = 1
        state["day"] = current_day + 1.0
        return True
   
    return False

def storyScreen():
    console = Console()
    layout = Layout()
    
    selected = 0
    
    # ensure starting scene
    if "scene_id" not in state:
        state["scene_id"] = 1
    
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
    
    def cdPanel():
        progress = Progress(
        TextColumn("[bold #F0B01D]{task.completed}/{task.total}[/bold #F0B01D]", style="yellow"),
        BarColumn(
            bar_width=50,
            style="bright_black",
            finished_style="#F0B01D"
        ),
        expand=True)
    
        task = progress.add_task("", total=MAX_CD)
        progress.update(task, completed=state.get("creative_drive", MAX_CD))
        
        delta = state.get("last_cd_change", 0)
        
        if delta is None:
            delta_text = Text("")
        elif delta > 0:
            delta_text = Text(f"+{delta}", style="bold green")
        elif delta < 0:
            delta_text = Text(f"{delta}", style="bold red")
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
    
    def buildScreen(scene):
        if not scene:
            return Panel("No scene.", box=box.MINIMAL)

        title = scene.get("title", "")
        body = scene.get("text", "")

        return Panel(
            Group(
                Align.center(
                    Text(title, style="bold #AE5182"),
                ),
                Text(body)
            ),
            title="Main Screen",
            box=box.MINIMAL,
            padding=(1, 2)
        )
    
    def buildChoices():
        nonlocal selected
        scene = getCurrentScene()
        choices = scene.get("choices", {}) if scene else {}
        choices_list = list(choices.keys())
        if not choices_list:
            # no choices: show continue prompt
            return Panel(Align.center(Text("Press Enter to continue")), title="Choices", border_style="#AE5182", padding=1)
        choicesContent = ""
        for i, key in enumerate(choices_list):
            text = choices[key].get("text", key)
            if i == selected:
                choicesContent += f"[bold #51AE7D]> {text} <[/bold #51AE7D]\n"
            else:
                choicesContent += f"  {text}\n"
        return Panel(choicesContent, 
                     title="Choices", 
                     border_style="#AE5182",
                     padding=1)
    
    layout["Bar"].update(cdPanel())
    layout["Day"].update(
        Panel(
            Align.center(Text(f"DAY {state.get('day')}", style="bold #AE5182"), vertical="middle"),
            box=box.MINIMAL)
    )
    layout["List"].update(historyPanel())
    layout["Controls"].update(keys())
    layout["Screen"].update(buildScreen(getCurrentScene()))
    layout["Choices"].update(buildChoices())
    
    clear()
    with Live(layout, console=console, refresh_per_second=20, screen=True):
        while True:
            key = msvcrt.getch()
            
            scene = getCurrentScene()
            choices = list(scene.get("choices", {}).keys()) if scene else []
            choices_len = max(1, len(choices))
            
            # Arrow keys (special codes)
            if key in (b'\xe0', b'\x00'):
                key = msvcrt.getch()
                if key == b'P':  # DOWN
                    selected = (selected + 1) % choices_len
                elif key == b'H':  # UP
                    selected = (selected - 1) % choices_len

                layout["Choices"].update(buildChoices())
    
            # Enter key
            elif key == b'\r':
                scene = getCurrentScene()
                if not scene:
                    # nothing to show, try transitioning
                    if dayTransition():
                        # reset and load next day scene
                        selected = 0
                        layout["Bar"].update(cdPanel())
                        layout["Day"].update(
                            Panel(
                                Align.center(Text(f"DAY {state.get('day')}", style="bold #AE5182"), vertical="middle"),
                                box=box.MINIMAL)
                        )
                        layout["Screen"].update(buildScreen(getCurrentScene()))
                        layout["Choices"].update(buildChoices())
                        layout["List"].update(historyPanel())
                        continue
                    else:
                        next_action = 'end'
                        break
    
                # if scene has choices
                if scene.get("choices"):
                    choice_key = choices[selected]
                    bridge = applyChoice(state, scene, choice_key)
    
                    # show bridge text briefly
                    layout["Screen"].update(Panel(Align.left(Text(f"[bold]{scene.get('title','')}[/bold]\n\n{bridge}")), box=box.MINIMAL, padding=1))
                    layout["Bar"].update(cdPanel())
                    layout["List"].update(historyPanel())
                    layout["Choices"].update(Panel(" ", title="Choices", border_style="#AE5182"))
                    time.sleep(0.8)
                    
                    # check for game over (creative drive depleted)
                    if state.get("creative_drive", 0) <= 0:
                        next_action = 'gameover'
                        break
    
                    # advance to next scene
                    state["scene_id"] = scene["id"] + 1
                    next_scene = getCurrentScene()
                    if not next_scene:
                        # end of day -> try transition
                        if dayTransition():
                            selected = 0
                            layout["Bar"].update(cdPanel())
                            layout["Day"].update(
                                Panel(
                                    Align.center(Text(f"DAY {state.get('day')}", style="bold #AE5182"), vertical="middle"),
                                    box=box.MINIMAL)
                            )
                            layout["Screen"].update(buildScreen(getCurrentScene()))
                            layout["Choices"].update(buildChoices())
                            layout["List"].update(historyPanel())
                            continue
                        else:
                            next_action = 'end'
                            break
                    else:
                        selected = 0
                        layout["Screen"].update(buildScreen(next_scene))
                        layout["Choices"].update(buildChoices())
                        layout["Bar"].update(cdPanel())
                        layout["List"].update(historyPanel())
    
                else:
                    # scene has no choices: treat Enter as continue
                    state["scene_id"] = scene["id"] + 1
                    next_scene = getCurrentScene()
                    if not next_scene:
                        if dayTransition():
                            selected = 0
                            layout["Bar"].update(cdPanel())
                            layout["Day"].update(
                                Panel(
                                    Align.center(Text(f"DAY {state.get('day')}", style="bold #AE5182"), vertical="middle"),
                                    box=box.MINIMAL)
                            )
                            layout["Screen"].update(buildScreen(getCurrentScene()))
                            layout["Choices"].update(buildChoices())
                            layout["List"].update(historyPanel())
                            continue
                        else:
                            next_action = 'end'
                            break
                    else:
                        selected = 0
                        layout["Screen"].update(buildScreen(next_scene))
                        layout["Choices"].update(buildChoices())
                        layout["Bar"].update(cdPanel())
                        layout["List"].update(historyPanel())
    
            # Esc key
            elif key == b'\x1b':
                exit()
    
    # Live closed here -> safe to show end/gameover screens
    clear()
    if next_action == 'gameover':
        gameOverScreen()
    elif next_action == 'end':
        endScreen()
    
def applyChoice(state, scene, choice_key):
    choice = scene["choices"][choice_key]

    cd_before = state["creative_drive"]
    
    state["creative_drive"] += choice["cd_change"]
    state["creative_drive"] = max(MIN_CD, min(MAX_CD, state["creative_drive"]))
   
    cd_after = state["creative_drive"]

    # only add flag if present
    if "flag" in choice:
        state["flags"].add(choice["flag"])

    state["history"].append(
        {
            "scene_id": scene["id"],
            "choice": choice_key,
            "cd_change": choice["cd_change"]
        }
    )
   
    state["last_cd_change"] = cd_after - cd_before

    return choice.get("bridge", "")


def endScreen():
    console = Console()
    layout = Layout()
    
    clear()
    
    layout.split_column(
        Layout(name="Top", size=11),
        Layout(name="Middle", size=8))
    
    # determine day title for ending display
    day_data = getDayData()
    day_title = day_data.get("title", "THE END") if day_data else "THE END"
    
    header = Panel(
        Align.center(
            Group(
                Align(Text(theEnd, style="bold #AE5182")),
                Align.center(Text(day_title, justify="center", style="bold #51AE7D")))),
        border_style="#5aa580",
        box=box.MINIMAL) 
    
    layout["Top"].update(header)
    
    endPrompt = header = Panel(
        Align.center(Text("Press any key to go back to menu.")),
        box=box.MINIMAL)
    
    layout["Middle"].update(endPrompt)
    
    print(layout)
    key = msvcrt.getch()
    resetGame()
    mainScreen()
    
def gameOverScreen():

    console = Console()
    layout = Layout()
    
    clear()
    
    layout.split_column(
        Layout(name="Top", size=11),
        Layout(name="Middle", size=8))
    
    header = Panel(
        Align.center(
            Group(
                Align(Text(gameOver, style="bold #AE5182")),
                Align.center(Text("Your energy has reached 0.", justify="center", style="bold #51AE7D")))),
        border_style="#5aa580",
        box=box.MINIMAL) 
    
    layout["Top"].update(header)
    
    endPrompt = header = Panel(
        Align.center(Text("Press any key to go back to menu.")),
        box=box.MINIMAL)
    
    layout["Middle"].update(endPrompt)
    
    print(layout)
    key = msvcrt.getch()
    resetGame()
    mainScreen()
    
    
