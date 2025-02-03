import os
import platform
import importlib
import time
import random
import logging
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from telethon import TelegramClient, events, __version__ as telethon_version
from telethon.sessions import StringSession
import config  # Import configuration file

# Initialize Rich Console
console = Console()

# Configure Logging
logging.basicConfig(
    format="[%(levelname)s] %(message)s",
    level=logging.INFO
)

# Cool ASCII Banner
BANNER = """
[bold cyan]
_____   __                          
___/  | / /________  _____  _________
__/   |/ /_  _ \_  |/_/  / / /_  ___/
_/  /|  / /  __/_>  < / /_/ /_(__  ) 
/_/  |_/  \___//_/|_| \__,_/ /____/  
       [bold green]CyberNexus - The Ultimate Telegram UserBot[/bold green]
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

# Initialize Telegram Client
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

# Start the bot
async def start_bot():
    console.print(BANNER)
    display_system_info()
    fake_loading()
    await client.start()
    console.print("[bold green]✅ CyberNexus Userbot is Online![/bold green]")

# Auto-load all plugins from "plugins" folder
def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)  # Create folder if not exists
    
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            try:
                importlib.import_module(f"plugins.{filename[:-3]}")
                
# Run the bot
with client:
    client.loop.run_until_complete(start_bot())
    load_plugins()  # Load all plugins
    client.run_until_disconnected()
