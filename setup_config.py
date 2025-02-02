import os
import sys
import time
from rich.console import Console
from rich.progress import track

# Console Styling
console = Console()

# ASCII Banner
BANNER = r"""
.__   __.  __________   ___  __    __       _______.
|  \ |  | |   ____\  \ /  / |  |  |  |     /       |
|   \|  | |  |__   \  V  /  |  |  |  |    |   (----`
|  . `  | |   __|   >   <   |  |  |  |     \   \    
|  |\   | |  |____ /  .  \  |  `--'  | .----)   |   
|__| \__| |_______/__/ \__\  \______/  |_______/    
"""

# Cool Loading Animation using "rich"
def loading_screen(task, seconds=2):
    for _ in track(range(seconds), description=f"[cyan]{task}...[/]"):
        time.sleep(1)

# Input Function with Validation
def get_input(prompt, is_numeric=False):
    while True:
        user_input = console.input(f"[bold cyan]➤ {prompt}: [/]").strip()
        if is_numeric and not user_input.isdigit():
            console.print("[bold red]⚠ Please enter a valid numeric ID![/]")
            continue
        if user_input:
            return user_input
        console.print("[bold red]⚠ This field cannot be empty. Try again![/]")

# Clear Screen & Display Banner
os.system("clear" if os.name == "posix" else "cls")
console.print(f"[bold blue]{BANNER}[/]\n", style="bold green")

loading_screen("🚀 Loading CyberNexus Setup")

console.print("\n[bold yellow]🚀 Welcome to CyberNexus Userbot Configuration 🚀[/]\n")

# Check if config.py already exists
if os.path.exists("config.py"):
    console.print("[bold red]⚠ Warning: 'config.py' already exists![/]\n")
    overwrite = console.input("[bold yellow]Do you want to overwrite it? (yes/no): [/]").strip().lower()
    if overwrite not in ["yes", "y"]:
        console.print("[bold green]✔ Keeping existing configuration![/]")
        sys.exit()

# Collect User Inputs
api_id = get_input("Enter your API ID", is_numeric=True)
api_hash = get_input("Enter your API HASH")
username = get_input("Enter your Username with @")
string_session = get_input("Enter your STRING SESSION")
owner_id = get_input("Enter your Telegram Owner ID (Your @USERNAME)")
cmd_hndlr = get_input("Enter your Command Handler (e.g., ! or .)")
deployer_name = get_input("Enter your Deployer Name")

# Save Configuration
config_content = f'''# CyberNexus Userbot Configuration

API_ID = {api_id}
API_HASH = "{api_hash}"
STRING_SESSION = "{string_session}"
USERNAME = "{username}"
OWNER_ID = {owner_id}
CMD_HNDLR = "{cmd_hndlr}"
DEPLOYER_NAME = "{deployer_name}"
'''

with open("config.py", "w") as config_file:
    config_file.write(config_content)

# Confirmation Message
loading_screen("Saving Configuration", 3)
console.print("\n[bold green]✅ Configuration saved successfully in 'config.py'! 🚀[/]\n")

# Ask User if they want to Start the Userbot
start_now = console.input("[bold cyan]🔄 Do you want to start CyberNexus now? (yes/no): [/]").strip().lower()

if start_now in ["yes", "y"]:
    console.print("\n[bold blue]🔄 Starting CyberNexus Userbot[/]\n")
    loading_screen("Initializing Userbot", 3)
    time.sleep(2)  # Small delay before execution
    os.system("python cybernexus.py")
else:
    console.print("\n[bold yellow]👋 Setup Completed! Start CyberNexus manually using:[/]")
    console.print("[bold cyan]python cybernexus.py[/]\n")
