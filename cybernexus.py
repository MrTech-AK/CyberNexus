import os
import platform
import importlib
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config  # Import configuration file

# Initialize Telegram Client using StringSession
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

# Start the client
async def start_bot():
    await client.start()
    print("✅ CyberNexus Userbot is Online!")

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
