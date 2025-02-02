import os
import platform
import importlib
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
        time.sleep(1)

# Clear Screen & Display Banner
os.system("clear" if os.name == "posix" else "cls")
console.print(f"[bold blue]{BANNER}[/]\n", style="bold green")
loading_screen("🚀 Hold Tight! Userbot about to Start 🔥")


# Initialize Telegram Client using StringSession
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

console.print("\n[bold blue]🔩 Setting Up CyberNexus[/]\n")
    loading_screen("Initializing Userbot", 5)

console.print("\n[bold blue]🔗 Getting all Plugins[/]\n")
    loading_screen("Initializing Userbot", 7)

console.print("\n[bold blue]🔄 Starting Assistant[/]\n")
    loading_screen("Initializing Userbot", 4)

console.print("\n[bold blue]🔥 All Process Completed ✅[/]\n")
    loading_screen("Initializing Userbot", 2)

console.print("\n[bold blue]CyberNexus Userbot Online 🚀[/]\n")
    loading_screen("Initializing Userbot", 2)

# Start the client
async def start_bot():
    await client.start()
    print("Thank You For Choosing CyberNexus 🔥")

# Auto-load all plugins from the "plugins" folder
def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)  # Create folder if not exists
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            importlib.import_module(f"plugins.{filename[:-3]}")

# Run the bot
with client:
    client.loop.run_until_complete(start_bot())
    load_plugins()  # Load all plugins
    client.run_until_disconnected()
