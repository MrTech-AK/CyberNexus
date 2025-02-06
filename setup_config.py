import os
import sys
import time
from rich.console import Console
from rich.progress import track
from rich.progress import Progress, SpinnerColumn, TextColumn

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

BANNER_MAIN = """
[bold cyan]
  _____   __                          
  ___/  | / /________  _____  _________
  __/   |/ / _  _\_  |/_/  / / /_  ___/
  _/  /|  / /  __/>  < / /_/ /_(__  ) 
  /_/  |_/ \___//_/|_| \__,_/ /____/  
       [bold green]CyberNexus - The Ultimate Telegram UserBot[/bold green]
[/bold cyan]
"""

# Fake Loading Steps
def fake_loading():
    steps = [
        "[cyan]🔌 Connecting to Telegram API...",
        "[cyan]🔒 Verifying CyberNexus Security Modules...",
        "[cyan]📡 Connecting to Secure Database...",
        "[cyan]⚙️  Optimizing System Performance...",
        "[cyan]🛠️  Initializing AI Engine...",
        "[cyan]📂 Importing CyberNexus Plugins...",
        "[cyan]🔄 Syncing User Data...",
        "[cyan]✅ Finalizing Setup..."
    ]

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        for step in steps:
            task = progress.add_task(step, total=1)
            time.sleep(random.randint(3, 7))  # Random delay (3-7 seconds)
            progress.update(task, advance=1)
            
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
deployer_name = get_input("Enter your Deployer Name")

# Save Configuration
config_content = f'''# CyberNexus Userbot Configuration

API_ID = {api_id}
API_HASH = "{api_hash}"
STRING_SESSION = "{string_session}"
USERNAME = "{username}"
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
    # Clear Screen & Display Banner
    os.system("clear" if os.name == "posix" else "cls")
    console.print(f"[bold blue]{BANNER_MAIN}[/]\n", style="bold green")
    console.print("\n[bold blue]🔄 Connecting CyberNexus Userbot[/]\n")
    fake_loading()
    loading_screen("Initializing Userbot", 3)  # Small delay before execution
    os.system("python cybernexus.py")
else:
    console.print("\n[bold yellow]👋 Setup Completed! Start CyberNexus manually using:[/]")
    console.print("[bold cyan]python cybernexus.py[/]\n")
