from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import
import asyncio


@client.on(events.NewMessage(pattern=r"^\.glitch (.+)$", outgoing=True))
async def glitch_effect(event):
    """CyberNexus Extended Glitch Effect"""

    text = event.pattern_match.group(1)
    effects = ["░", "▒", "▓", "█", "✨", "⚡", "💀", "👾"]
    
    for _ in range(10):  # Controls number of glitches
        glitched_text = "".join(char + effects[_ % len(effects)] for char in text)
        await event.edit(glitched_text)
        await asyncio.sleep(0.2)

    await event.edit(f"🛠 **Glitch Fixed!**\n🔹 `{text}`")  # Restores original text
