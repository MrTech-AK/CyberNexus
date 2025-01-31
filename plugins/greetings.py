from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

welcome_message = None
goodbye_message = None

@client.on(events.NewMessage(pattern=r"^\.setwelcome$", outgoing=True))
async def setwelcome(event):
    """Set the welcome message."""
    global welcome_message
    welcome_message = event.text.split(None, 1)[1] if len(event.text.split()) > 1 else "Welcome!"
    await event.edit(f"**Welcome message set to:** {welcome_message}")

@client.on(events.NewMessage(pattern=r"^\.clearwelcome$", outgoing=True))
async def clearwelcome(event):
    """Clear the welcome message."""
    global welcome_message
    welcome_message = None
    await event.edit("**Welcome message cleared.**")

@client.on(events.NewMessage(pattern=r"^\.getwelcome$", outgoing=True))
async def getwelcome(event):
    """Get the current welcome message."""
    if welcome_message:
        await event.edit(f"**Current welcome message:** {welcome_message}")
    else:
        await event.edit("**No welcome message set.**")

@client.on(events.NewMessage(pattern=r"^\.setgoodbye$", outgoing=True))
async def setgoodbye(event):
    """Set the goodbye message."""
    global goodbye_message
    goodbye_message = event.text.split(None, 1)[1] if len(event.text.split()) > 1 else "Goodbye!"
    await event.edit(f"**Goodbye message set to:** {goodbye_message}")

@client.on(events.NewMessage(pattern=r"^\.cleargoodbye$", outgoing=True))
async def cleargoodbye(event):
    """Clear the goodbye message."""
    global goodbye_message
    goodbye_message = None
    await event.edit("**Goodbye message cleared.**")

@client.on(events.NewMessage(pattern=r"^\.getgoodbye$", outgoing=True))
async def getgoodbye(event):
    """Get the current goodbye message."""
    if goodbye_message:
        await event.edit(f"**Current goodbye message:** {goodbye_message}")
    else:
        await event.edit("**No goodbye message set.**")

@client.on(events.NewMessage(pattern=r"^\.thankmembers (on|off)$", outgoing=True))
async def thankmembers(event):
    """Enable or disable the thank members message when someone joins."""
    status = event.pattern_match.group(1)
    if status == "on":
        # Enable thank you message logic
        await event.edit("**Thank members message enabled.**")
    else:
        # Disable thank you message logic
        await event.edit("**Thank members message disabled.**")
