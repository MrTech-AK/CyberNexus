from telethon import events
from cybernexus import client
import asyncio  # Use asyncio for async delays
import platform 

@client.on(events.NewMessage(pattern=r"^\.typing (.+)$", outgoing=True))
async def typing_effect(event):
    """CyberNexus Typing Effect Animation"""

    text = event.pattern_match.group(1)  # Get the text after .typing
    typing_message = ""

    for char in text:
        typing_message += char
        await event.edit(typing_message + "▌")  # Simulate typing cursor
        await asyncio.sleep(0.1)  # Adjust speed for realism

    await event.edit(typing_message)  # Remove cursor at the end
