import os
import importlib
import asyncio
import time
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config  # Import configuration file
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
        time.sleep(1)  # ✅ Ensure time.sleep is properly used

# Clear Screen & Display Banner
try:
    os.system("clear" if os.name == "posix" else "cls")
except Exception:
    pass

console.print(f"[bold blue]{BANNER}[/]\n", style="bold green")
loading_screen("🚀 Hold Tight! Userbot about to Start 🔥")

# Initialize Telegram Client using StringSession
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

console.print("\n[bold blue]🔩 Setting Up CyberNexus[/]\n")
loading_screen("🔩 Setting Up CyberNexus", 5)

console.print("\n[bold blue]🔗 Getting all Plugins[/]\n")
loading_screen("🔗 Getting all Plugins", 7)

console.print("\n[bold blue]🔄 Starting Assistant[/]\n")
loading_screen("🔄 Starting Assistant", 4)

console.print("\n[bold blue]🔥 Finalizing Setup[/]\n")
loading_screen("🔥 Finalizing Setup", 2)

console.print("\n[bold blue]CyberNexus Userbot Online 🚀[/]\n")
loading_screen("🚀 CyberNexus Userbot Online", 2)

# Start the client
async def start_bot():
    console.print("[bold green]🔄 Starting CyberNexus Userbot...[/]")
    await client.start()
    console.print("[bold green]✅ CyberNexus Userbot Started Successfully! 🔥[/]")

# Auto-load all plugins from the "plugins" folder
def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)  # Create folder if not exists

    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            importlib.import_module(f"plugins.{filename[:-3]}")

async def main():
    await start_bot()  # ✅ Start inside event loop
    load_plugins()
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())  # ✅ Correct event loop handling
