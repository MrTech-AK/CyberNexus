import os
import importlib
import platform
from telethon import TelegramClient, events
import config

# CyberNexus Banner
BANNER = f"""
╔══════════════════════════════════════════════╗
║                CYBERNEXUS USERBOT            
╠══════════════════════════════════════════════╣
║         Customizable, Fast, Secure           
║   Running on: {platform.system()} {platform.release()} ({platform.architecture()[0]})  
╚══════════════════════════════════════════════╝
"""

print(BANNER)

# Initialize CyberNexus Client
client = TelegramClient("cybernexus", config.API_ID, config.API_HASH).start(
    session=config.STRING_SESSION
)

# Plugin Loader
def load_plugins():
    plugin_path = "plugins"
    for filename in os.listdir(plugin_path):
        if filename.endswith(".py"):
            importlib.import_module(f"{plugin_path}.{filename[:-3]}")
            print(f"✅ Loaded plugin: {filename}")

# Run CyberNexus
if __name__ == "__main__":
    print(f"🔹 CyberNexus is starting on {platform.system()} {platform.release()}...")
    load_plugins()
    print("✅ All plugins loaded successfully!")
    print("🚀 CyberNexus is now running!")
    client.run_until_disconnected()
