from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Global banned users (for demonstration purposes)
global_banned_users = []

@client.on(events.NewMessage(pattern=r"^\.gpromote( (.*)|$)", outgoing=True))
async def gpromote(event):
    """Promote a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been globally promoted.**")

@client.on(events.NewMessage(pattern=r"^\.gdemote( (.*)|$)", outgoing=True))
async def gdemote(event):
    """Demote a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been globally demoted.**")

@client.on(events.NewMessage(pattern=r"^\.ungban( (.*)|$)", outgoing=True))
async def ungban(event):
    """Unban a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"**User {user} has been globally unbanned.**")

@client.on(events.NewMessage(pattern=r"^\.gban( (.*)|$)", outgoing=True))
async def gban(event):
    """Ban a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    global_banned_users.append(user)
    await event.edit(f"**User {user} has been globally banned.**")

@client.on(events.NewMessage(pattern=r"^\.g(admin|)cast( (.*)|$)", outgoing=True))
async def gcast(event):
    """Send a message globally to all groups or admins."""
    message = event.pattern_match.group(3) if event.pattern_match.group(3) else "No message provided"
    # Send message to all groups/admins (example logic, needs implementation)
    await event.edit(f"**Global broadcast message sent:**\n{message}")

@client.on(events.NewMessage(pattern=r"^\.gucast( (.*)|$)", outgoing=True))
async def gucast(event):
    """Send a message globally to all private chats."""
    message = event.pattern_match.group(1) if event.pattern_match.group(1) else "No message provided"
    # Send message to all private chats (example logic, needs implementation)
    await event.edit(f"**Global private message sent:**\n{message}")

@client.on(events.NewMessage(pattern=r"^\.gkick( (.*)|$)", outgoing=True))
async def gkick(event):
    """Kick a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    # Kick logic (example)
    await event.edit(f"**User {user} has been globally kicked.**")

@client.on(events.NewMessage(pattern=r"^\.gmute( (.*)|$)", outgoing=True))
async def gmute(event):
    """Mute a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    # Mute logic (example)
    await event.edit(f"**User {user} has been globally muted.**")

@client.on(events.NewMessage(pattern=r"^\.ungmute( (.*)|$)", outgoing=True))
async def ungmute(event):
    """Unmute a user globally."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    # Unmute logic (example)
    await event.edit(f"**User {user} has been globally unmuted.**")

@client.on(events.NewMessage(pattern=r"^\.listgban$", outgoing=True))
async def listgban(event):
    """List all globally banned users."""
    if global_banned_users:
        await event.edit(f"**Globally banned users:**\n" + "\n".join(global_banned_users))
    else:
        await event.edit("**No users are globally banned.**")

@client.on(events.NewMessage(pattern=r"^\.gstat( (.*)|$)", outgoing=True))
async def gstat(event):
    """Show global ban statistics."""
    await event.edit(f"**Global Ban Statistics:**\nTotal Banned Users: {len(global_banned_users)}")

@client.on(events.NewMessage(pattern=r"^\.gblacklist$", outgoing=True))
async def gblacklist(event):
    """Blacklist a user globally."""
    user = event.sender_id
    # Blacklist logic (example)
    await event.edit(f"**User {user} has been globally blacklisted.**")

@client.on(events.NewMessage(pattern=r"^\.ungblacklist$", outgoing=True))
async def ungblacklist(event):
    """Remove a user from the global blacklist."""
    user = event.sender_id
    # Remove blacklist logic (example)
    await event.edit(f"**User {user} has been removed from the global blacklist.**")
