from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import

@client.on(events.NewMessage(pattern=r"^.alive$", outgoing=True))
async def alive(event):
    cyber_alive_text = (
        "🌐 **ᴄʏʙᴇʀɴᴇxᴜs | ᴏɴʟɪɴᴇ** 🌐\n\n"
        f"✵ **Owner:** {config.DEPLOYER_NAME} 👑\n"
        "✵ **Nexus:** v1.0\n"
        "✵ **Py-Nexus:** 2025\n"
        "✵ **Uptime:** Aʟɪᴠᴇ & ᴡᴇʟʟ ⏳\n"
        f"✵ **Python:** v{platform.python_version()} 🐍\n"
        f"✵ **Telethon:** v{telethon.__version__} 📡\n"
        "✵ **Branch:** main ⚙️"
    )

    image_path = "images/CyberNexus_Alive.jpg"

    # Delete the command message
    await event.delete()

    # Send the image with the Alive text as a caption
    await client.send_file(event.chat_id, image_path, caption=cyber_alive_text)
