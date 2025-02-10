import os
import importlib
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config  # Import configuration file

# Initialize CyberNexus Userbot
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

# Initialize Contact Bot
bot = TelegramClient("CyberNexus_ContactBot", config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

# Start the Userbot
async def start_userbot():
    await client.start()
    print("✅ CyberNexus Userbot is Online!")

# Auto-load all userbot plugins from "plugins" folder
def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            importlib.import_module(f"plugins.{filename[:-3]}")

# Run both bots
async def main():
    await start_userbot()
    print("✅ CyberNexus Contact Bot is Online!")
    load_plugins()  # Load all plugins for Userbot
    await asyncio.gather(client.run_until_disconnected(), bot.run_until_disconnected())

with client, bot:
    client.loop.run_until_complete(main())
