from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import

@client.on(events.NewMessage(pattern=r"^\.glitch (.+)$", outgoing=True))
def glitch_effect(event):
    """CyberNexus Extended Glitch Effect"""
    
    text = event.pattern_match.group(1)
    glitched_text = text
    effects = ["░", "▒", "▓", "█", "✨", "⚡", "💀", "👾"]

    for _ in range(20):  # More Glitches
        glitched_text = "".join([char + effects[_ % len(effects)] for char in text])
        event.edit(glitched_text)
        time.sleep(0.2)

    event.edit(text)  # Restore original text
