from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon

# Alive message plugin
@client.on(events.NewMessage(pattern=f"^{config.CMD_HNDLR}alive"))
async def alive(event):
    uptime = time.time() - client.start_time  # Calculate uptime
    uptime_str = f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m {int(uptime % 60)}s"
    
    # Get Python and Telethon version
    python_version = sys.version.split(" ")[0]  # Get Python version (e.g., 3.9.1)
    telethon_version = telethon.__version__  # Get Telethon version
    
    alive_text = f"""
    ᴄʏʙᴇʀɴᴇxᴜs | ᴏɴʟɪɴᴇ 🌐

    ✵ **Owner - {config.DEPLOYER_NAME} 👑**  
    ✵ **Nexus:** v1.0  
    ✵ **Py-Nexus:** 2025  
    ✵ **Uptime:** Aʟɪᴠᴇ & ᴡᴇʟʟ ⏳  
    ✵ **Python:** v{python_version} 🐍  
    ✵ **Telethon:** v{telethon_version} 📡  
    ✵ **Branch:** main ⚙️
    
    ⏱️ **Uptime:** {uptime_str}
    """
    
    # Edit the command message instead of sending a new one
    await event.edit(alive_text)
