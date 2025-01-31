from telethon import TelegramClient, events
import config
import os
import importlib

# Initialize the Telethon client
client = TelegramClient(
    session=config.STRING_SESSION, 
    api_id=config.API_ID, 
    api_hash=config.API_HASH
)

# Load plugins dynamically
async def load_plugins():
    plugin_folder = "plugins"
    if not os.path.exists(plugin_folder):
        os.mkdir(plugin_folder)
    
    for file in os.listdir(plugin_folder):
        if file.endswith(".py"):
            plugin_name = file[:-3]  # Remove .py extension
            importlib.import_module(f"plugins.{plugin_name}")  # Dynamically import plugins

# Start the bot
async def start_bot():
    await client.start()
    print("CyberNexus Userbot is now running!")
    await load_plugins()
    await client.run_until_disconnected()

# Event to confirm bot startup
@client.on(events.NewMessage(pattern=f"^{config.CMD_HNDLR}start"))
async def start_message(event):
    await event.edit("CʏʙᴇʀNᴇxᴜs ɪs ɴᴏᴡ ᴏɴʟɪɴᴇ!")

# Run the bot
if __name__ == "__main__":
    client.loop.run_until_complete(start_bot())
