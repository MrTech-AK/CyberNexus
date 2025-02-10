import os
import importlib
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config  # Import configuration file

# Initialize CyberNexus Userbot (Using StringSession)
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

# Initialize Contact Bot with a separate session file
bot_session_file = "contact_bot_session.session"
bot = TelegramClient(bot_session_file, config.API_ID, config.API_HASH)

# Start the Userbot
async def start_userbot():
    await client.start()
    print("✅ CyberNexus Userbot is Online!")

# Start the Contact Bot
async def start_contact_bot():
    await bot.start(bot_token=config.BOT_TOKEN)
    print("✅ CyberNexus Contact Bot is Online!")

# Auto-load all userbot plugins from "plugins" folder
def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)

    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            importlib.import_module(f"plugins.{filename[:-3]}")

# Run both bots in an event loop
async def main():
    await start_userbot()
    await start_contact_bot()
    load_plugins()  # Load all plugins for Userbot
    print("🚀 Both CyberNexus Userbot & Contact Bot are Running!")
    await asyncio.gather(client.run_until_disconnected(), bot.run_until_disconnected())

# Handle event loop properly in Termux & other environments
loop = asyncio.get_event_loop()
if loop.is_running():
    loop.create_task(main())  # If the loop is already running, schedule the task
else:
    loop.run_until_complete(main())  # If the loop is not running, start it normally
