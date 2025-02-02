import asyncio
from telethon import events, Button
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from config import bot  # Ensure bot is initialized from config.py

# ─────────── 🔹 HELP MENU ─────────── #
ADMIN_HELP_TEXT = (
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
    "➤ `.admin purge` – Delete multiple messages in bulk.\n"
    "➤ `.admin purgeme <count>` – Delete your last `<count>` messages.\n\n"
    "**Pinned Messages:**\n"
    "➤ `.admin pinned` – Show the most recently pinned message.\n"
    "➤ `.admin listpinned` – List all pinned messages in the chat."
)

# ─────────── 🔹 INLINE ADMIN HELP ─────────── #
@bot.on(events.NewMessage(pattern="^.adminhelp$"))
async def admin_help(event):
    await event.reply("🛠 **CyberNexus Admin Tools Help**", buttons=[
        [Button.inline("👤 User Management", data="admin_user")],
        [Button.inline("📝 Message Management", data="admin_msg")],
        [Button.inline("📌 Pinned Messages", data="admin_pinned")],
        [Button.inline("🔙 Close", data="admin_close")]
    ])

@bot.on(events.CallbackQuery(data=b"admin_user"))
async def admin_user_help(event):
    await event.edit(
        "**User Management:**\n"
        "➤ `.admin promote` – Promote a user to admin.\n"
        "➤ `.admin demote` – Demote an admin to a normal user.\n"
        "➤ `.admin ban` – Ban a user from the group.\n"
        "➤ `.admin unban` – Unban a user.\n"
        "➤ `.admin kick` – Kick a user from the group.\n"
        "➤ `.admin tban <time>` – Temporarily ban a user.",
        buttons=[Button.inline("🔙 Back", data="admin_back")]
    )

@bot.on(events.CallbackQuery(data=b"admin_back"))
async def admin_back(event):
    await admin_help(event)

@bot.on(events.CallbackQuery(data=b"admin_close"))
async def admin_close(event):
    await event.delete()

# ─────────── 👤 USER MANAGEMENT COMMANDS ─────────── #
@bot.on(events.NewMessage(pattern=r"^.admin promote$"))
async def promote(event):
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        await bot(EditAdminRequest(
            event.chat_id, reply_msg.sender_id,
            ChatAdminRights(post_messages=True, add_admins=False, invite_users=True, ban_users=True, delete_messages=True, pin_messages=True),
            "CyberNexus Admin"
        ))
        await event.reply(f"✅ **User Promoted to Admin**: `{reply_msg.sender_id}`")

@bot.on(events.NewMessage(pattern=r"^.admin demote$"))
async def demote(event):
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        await bot(EditAdminRequest(
            event.chat_id, reply_msg.sender_id,
            ChatAdminRights(),  # Remove all permissions
            ""
        ))
        await event.reply(f"🚫 **Admin Demoted**: `{reply_msg.sender_id}`")

@bot.on(events.NewMessage(pattern=r"^.admin ban$"))
async def ban(event):
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        await bot.edit_permissions(event.chat_id, reply_msg.sender_id, view_messages=False)
        await event.reply(f"🚨 **User Banned**: `{reply_msg.sender_id}`")

@bot.on(events.NewMessage(pattern=r"^.admin unban$"))
async def unban(event):
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        await bot.edit_permissions(event.chat_id, reply_msg.sender_id, view_messages=True)
        await event.reply(f"✅ **User Unbanned**: `{reply_msg.sender_id}`")

@bot.on(events.NewMessage(pattern=r"^.admin kick$"))
async def kick(event):
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        await bot.kick_participant(event.chat_id, reply_msg.sender_id)
        await event.reply(f"👞 **User Kicked**: `{reply_msg.sender_id}`")

# ─────────── 📝 MESSAGE MANAGEMENT COMMANDS ─────────── #
@bot.on(events.NewMessage(pattern="^.admin pin$"))
async def pin(event):
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        await msg.pin()
        await event.reply("📌 **Message Pinned!**")

@bot.on(events.NewMessage(pattern="^.admin unpin$"))
async def unpin(event):
    await bot.pin_message(event.chat_id, None)
    await event.reply("📌 **Unpinned Last Message!**")

@bot.on(events.NewMessage(pattern="^.admin purge$"))
async def purge(event):
    async for msg in bot.iter_messages(event.chat_id, min_id=event.message.id, reverse=True):
        await msg.delete()
    await event.delete()

@bot.on(events.NewMessage(pattern="^.admin purgeme (\d+)$"))
async def purge_me(event):
    count = int(event.pattern_match.group(1))
    async for msg in bot.iter_messages(event.chat_id, from_user=event.sender_id, limit=count):
        await msg.delete()

# ─────────── 📌 PINNED MESSAGE COMMANDS ─────────── #
@bot.on(events.NewMessage(pattern="^.admin pinned$"))
async def pinned(event):
    pinned_msg = await bot(GetPinnedMessageRequest(event.chat_id))
    if pinned_msg:
        await event.reply(f"📌 **Pinned Message:**\n{pinned_msg.message.message}")
    else:
        await event.reply("🚫 **No pinned messages found!**")

@bot.on(events.NewMessage(pattern="^.admin listpinned$"))
async def list_pinned(event):
    pinned_msgs = []
    async for msg in bot.iter_messages(event.chat_id, pinned=True):
        pinned_msgs.append(f"📌 {msg.text[:50]}..." if msg.text else "📌 [Media Message]")

    if pinned_msgs:
        await event.reply("\n".join(pinned_msgs))
    else:
        await event.reply("🚫 **No pinned messages found!**")

# Start bot
print("✅ CyberNexus Admin Tools Loaded...")
bot.run_until_disconnected()
