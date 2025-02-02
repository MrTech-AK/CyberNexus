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

BOTFATHER_ID = 93372553  # Official BotFather ID


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


async def create_bot():
    async with client.conversation("BotFather") as conv:
        console.print("[bold yellow]🤖 Creating a new bot...[/bold yellow]")
        loading_animation("Requesting BotFather", 3)

        # Start the bot creation process by sending the '/newbot' command
        await conv.send_message("/newbot")
        await conv.get_response()

        bot_name = "CyberNexus Contact Bot"  # Name for the new bot
        await conv.send_message(bot_name)
        await conv.get_response()

        # Fetch the bot username dynamically from the config file (USERNAME entered by user)
        bot_username = f"{config.USERNAME}_CyberNexus_Bot"  # Replace {USERNAME} with actual username
        await conv.send_message(bot_username)
        response = await conv.get_response()

        # Handle the case where the bot username is already taken
        if "Sorry" in response.text:
            console.print("[bold red]⚠ Bot username already taken! Try again.[/bold red]")
            return None

        # Extract the bot token from the response
        bot_token = response.text.split("Use this token to access the HTTP API:")[1].split("\n")[0].strip()
        console.print(f"[bold green]✅ Bot Created Successfully! Token: {bot_token}[/bold green]")

        return bot_token


async def configure_bot(bot_token):
    async with client.conversation("BotFather") as conv:
        console.print("[bold cyan]⚙ Configuring bot...[/bold cyan]")
        loading_animation("Setting description", 2)

        await conv.send_message(f"/setdescription {bot_token}")
        await conv.get_response()
        await conv.send_message("🤖 This is a CyberNexus-powered contact bot.")
        await conv.get_response()

        loading_animation("Updating bot info", 2)
        await conv.send_message(f"/setabouttext {bot_token}")
        await conv.get_response()
        await conv.send_message("⚡ CyberNexus: The Future of Telegram Automation")
        await conv.get_response()

        loading_animation("Adding bot commands", 2)
        await conv.send_message(f"/setcommands {bot_token}")
        await conv.get_response()
        await conv.send_message("start - Start the bot\nhelp - Get help")
        await conv.get_response()

        console.print("[bold green]✅ Bot Configuration Completed![/bold green]")


async def run_contact_bot():
    console.print("[bold blue]📩 Starting CyberNexus Contact Bot...[/bold blue]")
    os.system("python contact_bot.py")  # Run the Contact Bot


async def main():
    console.print("[bold blue]🔹 CyberNexus Userbot is Booting... 🔹[/bold blue]\n")

    loading_animation("Starting Userbot", 3)

    async with client:
        await start_bot()

        bot_token = await create_bot()
        if bot_token:
            await configure_bot(bot_token)

        load_plugins()  # Load plugins

        console.print("[bold green]🚀 CyberNexus is Running![/bold green]")

        # Start the Contact Bot
        await asyncio.create_task(run_contact_bot())

        await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
