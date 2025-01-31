from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.font( (.*)|$)", outgoing=True))
async def fontgen(event):
    """Generate text in Tʜɪs font."""
    text = event.pattern_match.group(1) if event.pattern_match.group(1) else "No text provided."
    font_text = ''.join([chr(ord(c) - 32 + 0x1D00) for c in text])  # Transforming to Tʜɪs font
    await event.edit(f"**Generated text in Tʜɪs font:**\n{font_text}")
