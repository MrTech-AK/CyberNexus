from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.help_mute$", outgoing=True))
async def help_mute(event):
    """Sends a help message explaining how to use the mute/unmute features."""
    help_message = (
        "🔇 **Mute/Unmute Help** 🔇\n\n"
        "Welcome to the **Mute/Unmute** guide! Here's how to use it:\n\n"
        "1. **Mute a user in DMs**: Use `.dmute <username>` to mute a user in direct messages.\n"
        "2. **Unmute a user in DMs**: Use `.undmute <username>` to unmute a user in direct messages.\n"
        "3. **Temporarily mute a user**: Use `.tmute` to temporarily mute yourself or someone.\n"
        "4. **Mute a user**: Use `.mute <username>` to mute a user in your group or chat.\n"
        "5. **Unmute a user**: Use `.unmute <username>` to unmute a previously muted user.\n\n"
        "🔊 **Important**: You can mute/unmute users in group chats or direct messages using the above commands.\n\n"
        "💡 **Pro Tip**: Use these commands to maintain a quiet environment or give someone a temporary break! 😎"
    )
    await event.edit(help_message)

@client.on(events.NewMessage(pattern=r"^\.dmute( (.*)|$)", outgoing=True))
async def dmute(event):
    """Mute a user in direct messages."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"🔇 **User {user} has been muted in DMs.**")

@client.on(events.NewMessage(pattern=r"^\.undmute( (.*)|$)", outgoing=True))
async def undmute(event):
    """Unmute a user in direct messages."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"🔊 **User {user} has been unmuted in DMs.**")

@client.on(events.NewMessage(pattern=r"^\.tmute$", outgoing=True))
async def tmute(event):
    """Temporarily mute a user."""
    user = event.sender_id
    await event.edit(f"🔇 **User {user} has been temporarily muted.**")

@client.on(events.NewMessage(pattern=r"^\.unmute( (.*)|$)", outgoing=True))
async def unmute(event):
    """Unmute a user."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"🔊 **User {user} has been unmuted.**")

@client.on(events.NewMessage(pattern=r"^\.mute( (.*)|$)", outgoing=True))
async def mute(event):
    """Mute a user."""
    user = event.pattern_match.group(1) if event.pattern_match.group(1) else event.sender_id
    await event.edit(f"🔇 **User {user} has been muted.**")
