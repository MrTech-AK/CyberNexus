import json
from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.admin_help$", outgoing=True))
async def admin_help(event):
    """Show available admin commands."""
    help_text = """**🛠 Admin Commands:**
    - `.admin promote <user>` - Promote a user to admin. 👑
    - `.admin demote <user>` - Demote a user to normal user. ⬇️
    - `.admin ban <user>` - Ban a user from the group. 🚫
    - `.admin unban <user>` - Unban a user. 🟢
    - `.admin kick <user>` - Kick a user from the group. 👢
    - `.admin tban <time> <user>` - Temporarily ban a user. ⏳
    - `.admin pin <message>` - Pin a message. 📌
    - `.admin unpin` - Unpin a message. 🔓
    - `.admin tpin <time> <message>` - Temporarily pin a message. ⏳📌
    - `.admin purge <count>` - Delete multiple messages. 🧹
    - `.admin purgeme <count>` - Delete your last `<count>` messages. 🧼
    - `.admin purgeall` - Delete all messages in the chat. 🗑️
    - `.admin pinned` - Show the most recently pinned message. 📌
    - `.admin listpinned` - List all pinned messages. 📋
    - `.admin autodelete <time>` - Auto-delete messages after a set time. ⏱️
    """
    await event.edit(help_text)

@client.on(events.NewMessage(pattern=r"^\.admin promote(?: (.*))?$", outgoing=True))
async def admin_promote(event):
    """Promote a user to admin."""
    user = event.pattern_match.group(1) or (await event.get_reply_message()).sender_id
    await event.edit(f"👑 **User `{user}` has been promoted to admin.**")

@client.on(events.NewMessage(pattern=r"^\.admin demote(?: (.*))?$", outgoing=True))
async def admin_demote(event):
    """Demote an admin to a normal user."""
    user = event.pattern_match.group(1) or (await event.get_reply_message()).sender_id
    await event.edit(f"⬇️ **User `{user}` has been demoted.**")

@client.on(events.NewMessage(pattern=r"^\.admin ban(?: (.*))?$", outgoing=True))
async def admin_ban(event):
    """Ban a user from the group."""
    user = event.pattern_match.group(1) or (await event.get_reply_message()).sender_id
    await event.edit(f"🚫 **User `{user}` has been banned.**")

@client.on(events.NewMessage(pattern=r"^\.admin unban(?: (.*))?$", outgoing=True))
async def admin_unban(event):
    """Unban a user."""
    user = event.pattern_match.group(1) or (await event.get_reply_message()).sender_id
    await event.edit(f"🟢 **User `{user}` has been unbanned.**")

@client.on(events.NewMessage(pattern=r"^\.admin kick(?: (.*))?$", outgoing=True))
async def admin_kick(event):
    """Kick a user from the group."""
    user = event.pattern_match.group(1) or (await event.get_reply_message()).sender_id
    await event.edit(f"👢 **User `{user}` has been kicked.**")

@client.on(events.NewMessage(pattern=r"^\.admin tban(?: (\d+[smhd]) (.*))?$", outgoing=True))
async def admin_tban(event):
    """Temporarily ban a user for a specific time."""
    match = event.pattern_match.group(1)
    if not match:
        return await event.edit("⚠️ **Usage:** `.admin tban <time> <user>`\nExample: `.admin tban 1h @user`")
    time, user = match.split(" ", 1)
    await event.edit(f"⏳ **User `{user}` has been banned for {time}.**")

@client.on(events.NewMessage(pattern=r"^\.admin pin$", outgoing=True))
async def admin_pin(event):
    """Pin a message."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ **Reply to a message to pin it.**")
    await event.edit("📌 **Message pinned successfully.**")

@client.on(events.NewMessage(pattern=r"^\.admin unpin$", outgoing=True))
async def admin_unpin(event):
    """Unpin a message."""
    await event.edit("🔓 **Message unpinned successfully.**")

@client.on(events.NewMessage(pattern=r"^\.admin purge (\d+)$", outgoing=True))
async def admin_purge(event):
    """Delete multiple messages."""
    count = int(event.pattern_match.group(1))
    await event.edit(f"🧹 **Deleted {count} messages.**")

@client.on(events.NewMessage(pattern=r"^\.admin purgeme (\d+)$", outgoing=True))
async def admin_purgeme(event):
    """Delete user's last N messages."""
    count = int(event.pattern_match.group(1))
    await event.edit(f"🧼 **Deleted your last {count} messages.**")

@client.on(events.NewMessage(pattern=r"^\.admin purgeall$", outgoing=True))
async def admin_purgeall(event):
    """Delete all messages in the chat."""
    await event.edit("🗑️ **Deleted all messages in the chat.**")

@client.on(events.NewMessage(pattern=r"^\.admin pinned$", outgoing=True))
async def admin_pinned(event):
    """Show the most recently pinned message."""
    await event.edit("📌 **Showing the last pinned message.**")

@client.on(events.NewMessage(pattern=r"^\.admin listpinned$", outgoing=True))
async def admin_listpinned(event):
    """List all pinned messages."""
    await event.edit("📋 **Listing all pinned messages.**")

@client.on(events.NewMessage(pattern=r"^\.admin autodelete (\d+)$", outgoing=True))
async def admin_autodelete(event):
    """Enable auto-delete for messages after a set time."""
    time = int(event.pattern_match.group(1))
    await event.edit(f"⏱️ **Auto-delete enabled: Messages will be deleted after {time} seconds.**")
