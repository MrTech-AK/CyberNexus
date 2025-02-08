from telethon import events
from cybernexus import client
import asyncio  # ✅ Use asyncio for proper async handling
import platform 

@client.on(events.NewMessage(pattern=r"^\.timetravel$", outgoing=True))
async def time_travel(event):
    """CyberNexus Time Travel Animation"""

    travel_steps = [
        "🔮 **Activating Time Machine...**",
        "⚡ **Generating Wormhole...**",
        "⏳ **Calibrating Timeline...**",
        "💥 **Entering Time Vortex... Hold Tight!**",
        "🌍 **Year 2025: AI Revolution is at its peak!**",
        "🚀 **Year 3000: Humans are now Cyborgs!**",
        "👽 **Year 10,000: Aliens have taken over Earth!**",
        "🕵️ **Year 1945: Oops! Landed in World War II! Escaping...**",
        "🛸 **Dinosaur Era: Running from a T-Rex!**",
        "🔥 **Future Glitch: Accidentally Created a Time Paradox!**",
        "🌌 **CyberNexus Stuck in a Black Hole...**",
        "🌀 **Time Machine Overheated! Initiating Emergency Return...**",
        "💫 **Boom! CyberNexus is Back in the Present!**",
        "✅ **Time Travel Successful!**"
    ]

    for step in travel_steps:
        await event.edit(step)  # ✅ Corrected `await`
        await asyncio.sleep(1)  # ✅ Replaced `time.sleep()` with `asyncio.sleep()`
