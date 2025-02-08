from telethon import events
from cybernexus import client
import asyncio
import platform 

@client.on(events.NewMessage(pattern=r"^\.handwrite (.+)$", outgoing=True))
async def handwritten_effect(event):
    """CyberNexus Handwritten Text Animation"""
    
    text = event.pattern_match.group(1)
    displayed_text = ""
    
    for char in text:
        displayed_text += char
        await event.edit(displayed_text + "✍️")
        await asyncio.sleep(0.2)
    
    await event.edit(displayed_text)  # Final message without ✍️
