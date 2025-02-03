import os
import sys
import platform
import importlib
import asyncio
import random
import logging
import traceback
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from telethon import TelegramClient, __version__ as telethon_version
from telethon.sessions import StringSession
import config  # Import configuration file
from rich import print 

# Initialize Rich Console
console = Console()

# Configure Logging
logging.basicConfig(
    format="[%(levelname)s] %(message)s",
    level=logging.INFO
)

# Cool ASCII Banner
BANNER = r"""
[bold cyan]
_____   __                          
___/  | / /________  _____  _________
__/   |/ /_  _ \\_  |/_/  / / /_  ___/
_/  /|  / /  __/_>  < / /_/ /_(__  ) 
/_/  |_/  \\___//_/|_| \\__,_/ /____/  
[/bold cyan]
"""

# Display system information
def display_system_info():
    os_info = f"{platform.system()} {platform.release()}"
    python_version = platform.python_version()
    console.print(f"🌐 [bold green]OS:[/bold green] {os_info}")
    console.print(f"🐍 [bold green]Python Version:[/bold green] {python_version}")
    console.print(f"📡 [bold green]Telethon Version:[/bold green] {telethon_version}\n")

# Fake Loading Steps
async def fake_loading():
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
            await asyncio.sleep(random.uniform(1.5, 3.0))  # Natural delay (1.5-3 sec)
            progress.update(task, advance=1)

# Initialize Telegram Client
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

# Auto-load all plugins from "plugins" folder
def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)  # Create folder if not exists
    
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            module_name = f"plugins.{filename[:-3]}"
            if module_name not in sys.modules:
                try:
                    importlib.import_module(module_name)
                    console.print(f"[bold green]✅ Loaded plugin: {filename}[/bold green]")
                except Exception as e:
                    console.print(f"[red]⚠️ Failed to load plugin {filename}[/red]")
                    console.print(traceback.format_exc())  # Print full error traceback

# Start the bot
async def start_bot():
    console.print(BANNER)
    display_system_info()
    await fake_loading()
    console.print("[bold green]✅ CyberNexus Userbot is Online![/bold green]")

# Run the bot
async def main():
    await client.start()
    await start_bot()
    load_plugins()  # Load all plugins
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
