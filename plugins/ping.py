from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import

@client.on(events.NewMessage(pattern=r"^.ping$", outgoing=True))
async def ping(event):
    start = time.time()
    await event.edit("Pɪɴɢɪɴɢ... ⏳")
    end = time.time()
    ping_ms = (end - start) * 1000

    await event.edit(f"🏓 **Pᴏɴɢ!**\n⏳ **{ping_ms:.2f}ms**")
