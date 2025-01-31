from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^.admin$", outgoing=True))
async def admin_help(event):
    help_text = (
        "🔹 **CyberNexus Admin Tools** 🔹\n\n"
        "**User Management:**\n"
        "➤ `.admin promote` – Promote a user to admin.\n"
        "➤ `.admin demote` – Demote an admin to a normal user.\n"
        "➤ `.admin ban` – Ban a user from the group.\n"
        "➤ `.admin unban` – Unban a user.\n"
        "➤ `.admin kick` – Kick a user from the group.\n"
        "➤ `.admin tban <time>` – Temporarily ban a user.\n\n"
        "**Message Management:**\n"
        "➤ `.admin pin` – Pin a message.\n"
        "➤ `.admin unpin` – Unpin the last pinned message.\n"
        "➤ `.admin tpin <time>` – Temporarily pin a message.\n"
        "➤ `.admin purge` – Delete multiple messages in bulk.\n"
        "➤ `.admin purgeme <count>` – Delete your last `<count>` messages.\n"
        "➤ `.admin purgeall` – Delete **all** messages in the chat.\n\n"
        "**Pinned Messages:**\n"
        "➤ `.admin pinned` – Show the most recently pinned message.\n"
        "➤ `.admin listpinned` – List all pinned messages in the chat.\n\n"
        "**Auto Management:**\n"
        "➤ `.admin autodelete <time>` – Auto-delete messages after a set time.\n"
    )
    await event.edit(help_text)

@client.on(events.NewMessage(pattern=r"^.admin promote$", outgoing=True))
async def promote(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ Reply to a user to promote them!")
    await client.edit_admin(event.chat_id, reply.sender_id, is_admin=True)
    await event.edit(f"✅ {reply.sender.first_name} is now an Admin!")

@client.on(events.NewMessage(pattern=r"^.admin demote$", outgoing=True))
async def demote(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ Reply to a user to demote them!")
    await client.edit_admin(event.chat_id, reply.sender_id, is_admin=False)
    await event.edit(f"❌ {reply.sender.first_name} has been demoted.")

@client.on(events.NewMessage(pattern=r"^.admin ban$", outgoing=True))
async def ban(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ Reply to a user to ban them!")
    await client.edit_permissions(event.chat_id, reply.sender_id, view_messages=False)
    await event.edit(f"🚨 {reply.sender.first_name} has been BANNED!")

@client.on(events.NewMessage(pattern=r"^.admin unban$", outgoing=True))
async def unban(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ Reply to a user to unban them!")
    await client.edit_permissions(event.chat_id, reply.sender_id, view_messages=True)
    await event.edit(f"✅ {reply.sender.first_name} has been Unbanned.")

@client.on(events.NewMessage(pattern=r"^.admin kick$", outgoing=True))
async def kick(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ Reply to a user to kick them!")
    await client.kick_participant(event.chat_id, reply.sender_id)
    await event.edit(f"🚪 {reply.sender.first_name} has been kicked.")

@client.on(events.NewMessage(pattern=r"^.admin tban (\d+)$", outgoing=True))
async def tban(event):
    reply = await event.get_reply_message()
    duration = int(event.pattern_match.group(1))
    if not reply:
        return await event.edit("⚠️ Reply to a user to temporarily ban them!")
    await client.edit_permissions(event.chat_id, reply.sender_id, view_messages=False)
    await event.edit(f"🚨 {reply.sender.first_name} has been banned for {duration} seconds.")
    time.sleep(duration)
    await client.edit_permissions(event.chat_id, reply.sender_id, view_messages=True)
    await event.respond(f"✅ {reply.sender.first_name} has been unbanned automatically.")

@client.on(events.NewMessage(pattern=r"^.admin purge$", outgoing=True))
async def purge(event):
    messages = []
    async for msg in client.iter_messages(event.chat_id, min_id=event.id):
        messages.append(msg.id)
    await client.delete_messages(event.chat_id, messages)
    await event.edit("🗑️ Messages Purged!")

@client.on(events.NewMessage(pattern=r"^.admin purgeme (\d+)$", outgoing=True))
async def purgeme(event):
    count = int(event.pattern_match.group(1))
    async for msg in client.iter_messages(event.chat_id, from_user="me", limit=count):
        await msg.delete()
    await event.delete()

@client.on(events.NewMessage(pattern=r"^.admin pin$", outgoing=True))
async def pin(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("⚠️ Reply to a message to pin it!")
    await client.pin_message(event.chat_id, reply)
    await event.edit("📌 Message Pinned!")

@client.on(events.NewMessage(pattern=r"^.admin unpin$", outgoing=True))
async def unpin(event):
    await client.unpin_message(event.chat_id)
    await event.edit("📌 Last pinned message unpinned!")

@client.on(events.NewMessage(pattern=r"^.admin pinned$", outgoing=True))
async def pinned(event):
    msg = await client.get_pinned_message(event.chat_id)
    if msg:
        await event.edit(f"📌 **Pinned Message:**\n\n{msg.text}")
    else:
        await event.edit("⚠️ No pinned messages found!")

@client.on(events.NewMessage(pattern=r"^.admin listpinned$", outgoing=True))
async def listpinned(event):
    messages = []
    async for msg in client.iter_messages(event.chat_id, pinned=True):
        messages.append(msg.text)
    if messages:
        await event.edit("\n\n".join(messages))
    else:
        await event.edit("⚠️ No pinned messages found!")

@client.on(events.NewMessage(pattern=r"^.admin autodelete (\d+)$", outgoing=True))
async def autodelete(event):
    delay = int(event.pattern_match.group(1))
    await event.edit(f"⏳ Auto-deleting messages every {delay} seconds.")
    async for msg in client.iter_messages(event.chat_id):
        time.sleep(delay)
        await msg.delete()
