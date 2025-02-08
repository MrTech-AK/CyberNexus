from telethon import events
from cybernexus import client
import platform
import asyncio  # ✅ Use asyncio instead of time.sleep()

@client.on(events.NewMessage(pattern=r"^\.loading$", outgoing=True))
async def loading_animation(event):
    """CyberNexus Super Extended Loading Effect"""
    
    animation = [
        "`Loading [░░░░░░░░░░] 0%`",
        "`Loading [▓░░░░░░░░░] 5%`",
        "`Loading [▓▓░░░░░░░░] 10%`",
        "`Loading [▓▓▓░░░░░░░] 15%`",
        "`Loading [▓▓▓▓░░░░░░] 20%`",
        "`Loading [▓▓▓▓▓░░░░░] 30%`",
        "`Loading [▓▓▓▓▓▓▓░░░] 40%`",
        "`Loading [▓▓▓▓▓▓▓▓░░] 50%`",
        "`Loading [▓▓▓▓▓▓▓▓▓░] 60%`",
        "`Loading [▓▓▓▓▓▓▓▓░░░] 70%`",
        "`Loading [█████████░] 80%`",
        "`Loading [██████████] 90%`",
        "`Loading Complete... Finalizing`",
        "`✅ Loading Complete!`"
    ]

    for frame in animation:
        await event.edit(frame)  # ✅ Corrected `await`
        await asyncio.sleep(0.4)  # ✅ Replaced `time.sleep()` with `asyncio.sleep()`
