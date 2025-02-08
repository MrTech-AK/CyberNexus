from telethon import events
from cybernexus import client
import pyfiglet
import asyncio
import platform 

@client.on(events.NewMessage(pattern=r"^\.ascii (.+)$", outgoing=True))
async def ascii_art(event):
    """CyberNexus ASCII Art Generator (Speed Font)"""
    text = event.pattern_match.group(1)
    
    try:
        ascii_text = pyfiglet.figlet_format(text, font="speed")  # Speed font
        await event.edit(f"```\n{ascii_text}\n```")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")
