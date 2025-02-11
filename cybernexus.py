import os
import importlib
from telethon import TelegramClient, events
import config  # Import configuration file

# Ensure session storage folder exists
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# Initialize Userbot with separate session file
client = TelegramClient("sessions/userbot_session.sqlite", config.API_ID, config.API_HASH)

# Initialize Contact Bot with separate session file
bot = TelegramClient("sessions/contactbot_session.sqlite", config.API_ID, config.API_HASH)

async def start_userbot():
    await client.start()
    print("✅ CyberNexus Userbot is Online!")

async def start_contact_bot():
    await bot.start(bot_token=config.BOT_TOKEN)
    print("✅ CyberNexus Contact Bot is Online!")

# Auto-load all plugins from the "plugins" folder
async def load_plugins():
    plugins_path = "plugins"
    if not os.path.exists(plugins_path):
        os.makedirs(plugins_path)  # Create folder if not exists
    for filename in os.listdir(plugins_path):
        if filename.endswith(".py"):
            importlib.import_module(f"plugins.{filename[:-3]}")

async def main():
    await start_userbot()
    await start_contact_bot()
    await load_plugins()
    print("🚀 Both CyberNexus Userbot & Contact Bot are Running!")
    await client.run_until_disconnected()
    await bot.run_until_disconnected()

# Run the bot
with client, bot:
    client.loop.run_until_complete(main())
