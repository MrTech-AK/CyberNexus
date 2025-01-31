from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.dmute( (.*)|$)", outgoing=True))
async def dmute(event):
    """Mute a user in direct messages."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been muted in DMs.**")

@client.on(events.NewMessage(pattern=r"^\.undmute( (.*)|$)", outgoing=True))
async def undmute(event):
    """Unmute a user in direct messages."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been unmuted in DMs.**")

@client.on(events.NewMessage(pattern=r"^\.tmute$", outgoing=True))
async def tmute(event):
    """Temporarily mute a user."""
    user = event.sender_id
    await event.edit(f"**User {user} has been temporarily muted.**")

@client.on(events.NewMessage(pattern=r"^\.unmute( (.*)|$)", outgoing=True))
async def unmute(event):
    """Unmute a user."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been unmuted.**")

@client.on(events.NewMessage(pattern=r"^\.mute( (.*)|$)", outgoing=True))
async def mute(event):
    """Mute a user."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been muted.**")
