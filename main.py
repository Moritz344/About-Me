from rich.console import Console
from rich.panel import Panel
from termcolor import cprint
import os
import questionary
import time
import sys

console = Console()
def text_animation(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def show_panel():
    panel = Panel(
        "[bold red]Moritz Maier \n[/bold red]"
        "\n"
        "[bold green]Work:[/bold green] I'm still a student.\n"
        "[bold green]Support:[/bold green] If you like what I do you can support me here: "
        "[bold yellow]https://ko-fi.com/pennti[/bold yellow]\n"
        "[bold green]Github:[/bold green] [bold yellow]https://github.com/Moritz344\n[/bold yellow]"
        "[bold green]Projects: \n[/bold green]"
        "- Terminal-Emulator \n"
        "- Twitch Chat \n"
        "- Chat-App \n"
        "- ...\n"
        "\n"
        "[bold red]About \n[/bold red]"
        "Im a 16 year old guy who codes in his freetime. For [bold green]coding[/bold green] I use [bold yellow]nvim[/bold yellow] and I really enjoy and suffer using it. I mainly code in Python but maybe in the future I will try learning a new Programming Language. Also I have some experience in the shell from the overthewire Bandit Level which was really cool and I recommend.",
        title="About",
        title_align="right",
        border_style="bold blue",
        width=100,
        height=20
    )
    console.print(panel)

show_panel()

def user_input():
    answers = questionary.form(
        select = questionary.select("What do you want to do?",choices=["Send me an e-mail","Quit"])

    ).ask()

    selected_item = answers["select"]
    if selected_item == "Send me an e-mail":
        text_animation("Here is my e-mail: moritzmaier34@gmail.com")
        time.sleep(1)
        user_input()
    elif selected_item == "Quit":
        text_animation("Have a great day.")
    


user_input()
