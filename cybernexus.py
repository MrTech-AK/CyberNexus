import os
import importlib
import asyncio
import sys
import time
from rich.console import Console
from rich.progress import track
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config  # Import API credentials

console = Console()

# Initialize Telegram Client (Userbot)
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)


# Cool Loading Animation
def loading_animation(task, seconds=2):
    for _ in track(range(seconds), description=f"[cyan]{task}...[/]"):
        time.sleep(1)


async def start_bot():
    await client.start()
    console.print("[bold green]✅ CyberNexus Userbot is Online![/bold green]")


def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)  # Create folder if not exists
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            importlib.import_module(f"plugins.{filename[:-3]}")
            console.print(f"[bold cyan]📂 Loaded Plugin: {filename}[/bold cyan]")

async def main():
    console.print("[bold blue]🔹 CyberNexus Userbot is Booting... 🔹[/bold blue]\n")

    loading_animation("Starting Userbot", 3)

    async with client:
        await start_bot()

        load_plugins()  # Load plugins

        console.print("[bold green]🚀 CyberNexus is Running![/bold green]")

        # Start the Contact Bot
        await asyncio.create_task(run_contact_bot())

        await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
