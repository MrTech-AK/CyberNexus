from telethon import events
from cybernexus import client
import asyncio  # ✅ Use asyncio instead of time.sleep()
import platform 

@client.on(events.NewMessage(pattern=r"^\.selfdestruct$", outgoing=True))
async def self_destruct(event):
    """CyberNexus Self-Destruct Animation"""

    self_destruct_steps = [
        "💀 **CyberNexus Self-Destruct Protocol Activated!**",
        "🔒 **Encrypting All Files...**",
        "📡 **Sending Self-Destruct Code to Telegram Servers...**",
        "⚠ **Warning! Unauthorized Access Detected!**",
        "🔍 **Scanning for Escape Routes...**",
        "🛠 **Disabling Anti-Virus Protection...**",
        "💣 **Planting Explosive Scripts...**",
        "🔄 **Overriding System Security...**",
        "⚡ **Power Surge Initiated...**",
        "🔥 **WARNING! System Overload Detected!**",
        "⏳ **Self-Destruct Countdown: 10...**",
        "⏳ **Self-Destruct Countdown: 9...**",
        "⏳ **Self-Destruct Countdown: 8...**",
        "⏳ **Self-Destruct Countdown: 7...**",
        "⏳ **Self-Destruct Countdown: 6...**",
        "⏳ **Self-Destruct Countdown: 5...**",
        "⏳ **Self-Destruct Countdown: 4...**",
        "⏳ **Self-Destruct Countdown: 3...**",
        "⏳ **Self-Destruct Countdown: 2...**",
        "⏳ **Self-Destruct Countdown: 1...**",
        "💥 **BOOM!!! SYSTEM DESTROYED!** 💀🔥",
        "✅ **Just Kidding! CyberNexus is Unstoppable!** 😎"
    ]

    for step in self_destruct_steps:
        await event.edit(step)  # ✅ Corrected `await`
        await asyncio.sleep(1)  # ✅ Replaced `time.sleep()` with `asyncio.sleep()`
