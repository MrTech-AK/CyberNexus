import json
from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Load banned users from a file (persists between restarts)
BAN_FILE = "global_bans.json"

def load_banned_users():
    try:
        with open(BAN_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_banned_users():
    with open(BAN_FILE, "w") as f:
        json.dump(global_banned_users, f, indent=4)

global_banned_users = load_banned_users()

@client.on(events.NewMessage(pattern=r"^\.help_globaltools$", outgoing=True))
async def help_menu(event):
    """Display help menu with all available commands."""
    help_text = """
    **📜 ᴄʏʙᴇʀɴᴇxᴜs ʜᴇʟᴘ ᴍᴇɴᴜ 📜**
    **📝 Available Commands:**
    - `.gpromote [user]` : 🌟 Promote a user globally.
    - `.gdemote [user]` : 👎 Demote a user globally.
    - `.gban [user]` : 🚫 Ban a user globally.
    - `.ungban [user]` : ✅ Unban a user globally.
    - `.listgban` : 🔍 List all globally banned users.
    - `.gkick [user]` : 🦵 Kick a user globally.
    - `.gmute [user]` : 🔇 Mute a user globally.
    - `.ungmute [user]` : 🔊 Unmute a user globally.
    - `.gcast [message]` : 📢 Broadcast to all groups/admins.
    - `.gucast [message]` : 📩 Broadcast to all private chats.
    - `.gblacklist` : 🚫 Blacklist a user globally.
    - `.ungblacklist` : ✅ Remove a user from the blacklist.
    """
    await event.edit(help_text)

@client.on(events.NewMessage(pattern=r"^\.gban(?: (.*))?$", outgoing=True))
async def gban(event):
    """Ban a user globally."""
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1) or (reply.sender_id if reply else None)

    if not user:
        return await event.edit("⚠️ **Reply to a user or provide an ID to ban.**")

    user = str(user)  # Convert to string for storage consistency
    if user not in global_banned_users:
        global_banned_users.append(user)
        save_banned_users()
        await event.edit(f"🚫 **User `{user}` has been globally banned.**")
    else:
        await event.edit(f"⚠️ **User `{user}` is already globally banned.**")

@client.on(events.NewMessage(pattern=r"^\.ungban(?: (.*))?$", outgoing=True))
async def ungban(event):
    """Unban a user globally."""
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1) or (reply.sender_id if reply else None)

    if not user:
        return await event.edit("⚠️ **Reply to a user or provide an ID to unban.**")

    user = str(user)
    if user in global_banned_users:
        global_banned_users.remove(user)
        save_banned_users()
        await event.edit(f"✅ **User `{user}` has been globally unbanned.**")
    else:
        await event.edit(f"❌ **User `{user}` is not globally banned.**")

@client.on(events.NewMessage(pattern=r"^\.listgban$", outgoing=True))
async def listgban(event):
    """List all globally banned users."""
    if not global_banned_users:
        return await event.edit("🚫 **No users are globally banned.**")

    user_list = "\n".join(f"• `{user}`" for user in global_banned_users)
    await event.edit(f"🔍 **Globally Banned Users:**\n{user_list}")

@client.on(events.NewMessage(pattern=r"^\.gpromote(?: (.*))?$", outgoing=True))
async def gpromote(event):
    """Promote a user globally."""
    user = event.pattern_match.group(1) or event.sender_id
    await event.edit(f"🌟 **User `{user}` has been globally promoted!** 🎉")

@client.on(events.NewMessage(pattern=r"^\.gdemote(?: (.*))?$", outgoing=True))
async def gdemote(event):
    """Demote a user globally."""
    user = event.pattern_match.group(1) or event.sender_id
    await event.edit(f"👎 **User `{user}` has been globally demoted.** 😔")

@client.on(events.NewMessage(pattern=r"^\.gkick(?: (.*))?$", outgoing=True))
async def gkick(event):
    """Kick a user globally."""
    user = event.pattern_match.group(1) or event.sender_id
    await event.edit(f"🦵 **User `{user}` has been globally kicked.** 🚶‍♂️")

@client.on(events.NewMessage(pattern=r"^\.gmute(?: (.*))?$", outgoing=True))
async def gmute(event):
    """Mute a user globally."""
    user = event.pattern_match.group(1) or event.sender_id
    await event.edit(f"🔇 **User `{user}` has been globally muted.** 🔕")

@client.on(events.NewMessage(pattern=r"^\.ungmute(?: (.*))?$", outgoing=True))
async def ungmute(event):
    """Unmute a user globally."""
    user = event.pattern_match.group(1) or event.sender_id
    await event.edit(f"🔊 **User `{user}` has been globally unmuted.** 🗣️")

@client.on(events.NewMessage(pattern=r"^\.gcast(?: (.*))?$", outgoing=True))
async def gcast(event):
    """Broadcast a message to all groups."""
    message = event.pattern_match.group(1) or "No message provided"
    await event.edit(f"📢 **Global Broadcast:**\n{message}")

@client.on(events.NewMessage(pattern=r"^\.gucast(?: (.*))?$", outgoing=True))
async def gucast(event):
    """Broadcast a message to all private chats."""
    message = event.pattern_match.group(1) or "No message provided"
    await event.edit(f"📩 **Global Private Broadcast:**\n{message}")

@client.on(events.NewMessage(pattern=r"^\.gblacklist$", outgoing=True))
async def gblacklist(event):
    """Blacklist a user globally."""
    user = event.sender_id
    await event.edit(f"🚫 **User `{user}` has been globally blacklisted.** 🔒")

@client.on(events.NewMessage(pattern=r"^\.ungblacklist$", outgoing=True))
async def ungblacklist(event):
    """Remove a user from the global blacklist."""
    user = event.sender_id
    await event.edit(f"✅ **User `{user}` has been removed from the global blacklist.** 🌐")
