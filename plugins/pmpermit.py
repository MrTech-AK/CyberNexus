from telethon import events
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from cybernexus import client
import json
import os
import config
import time
import sys
import telethon
import platform

# File to store approved users
APPROVED_USERS_FILE = "approved_users.json"

# Load approved users safely
def load_approved_users():
    if os.path.exists(APPROVED_USERS_FILE):
        try:
            with open(APPROVED_USERS_FILE, "r") as f:
                return set(json.load(f))
        except json.JSONDecodeError:
            return set()  # Reset if JSON is corrupted
    return set()

# Save approved users
def save_approved_users():
    with open(APPROVED_USERS_FILE, "w") as f:
        json.dump(list(approved_users), f)

approved_users = load_approved_users()
unapproved_counts = {}

# 📚 Help Command
@client.on(events.NewMessage(pattern=r"^\.help_pmpermit$", outgoing=True))
async def pmpermit_help(event):
    help_message = (
        "📚 **PM Permit Help** 📚\n\n"
        "🛑 **Commands:**\n"
        "✅ `.a` - Approve a user\n"
        "🚫 `.da` - Disapprove a user\n"
        "🔒 `.block <user_id>` - Block a user\n"
        "🔓 `.unblock <user_id>` - Unblock a user\n"
        "📜 `.listapproved` - List all approved users\n\n"
        "⚠️ **Warning:** Spamming = Block! 🚫 5 messages = Auto block! 🔥"
    )
    await event.edit(help_message)

# ✅ Approve a User
@client.on(events.NewMessage(pattern=r"^\.a$", outgoing=True))
async def approve_user(event):
    global approved_users
    reply = await event.get_reply_message()
    user = reply.sender_id if reply else event.sender_id

    if user in approved_users:
        return await event.edit("✅ **User is already approved.**")

    approved_users.add(user)
    save_approved_users()
    
    await event.edit(f"✅ **Approved user:** `{user}`")

# 🚫 Disapprove a User
@client.on(events.NewMessage(pattern=r"^\.da$", outgoing=True))
async def disapprove_user(event):
    global approved_users
    reply = await event.get_reply_message()
    user = reply.sender_id if reply else event.sender_id

    if user in approved_users:
        approved_users.remove(user)
        save_approved_users()
        await event.edit(f"🚫 **User disapproved:** `{user}`")
    else:
        await event.edit("🚫 **User is already unapproved.**")

# 🚫 Block a User
@client.on(events.NewMessage(pattern=r"^\.block( (.*)|$)", outgoing=True))
async def block_user(event):
    global approved_users
    reply = await event.get_reply_message()
    user = event.pattern_match.group(2) or (reply.sender_id if reply else None)
    
    if not user:
        return await event.edit("❌ **Reply to a user or specify their ID to block them.**")
    
    try:
        user = int(user)
    except ValueError:
        return await event.edit("❌ **Invalid user ID!**")

    await client(BlockRequest(user))
    approved_users.discard(user)
    save_approved_users()

    await event.edit(f"🚫 **Blocked user:** `{user}`")

# ✅ Unblock a User
@client.on(events.NewMessage(pattern=r"^\.unblock( (.*)|$)", outgoing=True))
async def unblock_user(event):
    global approved_users
    reply = await event.get_reply_message()
    user = event.pattern_match.group(2) or (reply.sender_id if reply else None)
    
    if not user:
        return await event.edit("❌ **Reply to a user or specify their ID to unblock them.**")
    
    try:
        user = int(user)
    except ValueError:
        return await event.edit("❌ **Invalid user ID!**")

    await client(UnblockRequest(user))
    approved_users.add(user)
    save_approved_users()

    await event.edit(f"✅ **Unblocked user:** `{user}`")

# 📜 List Approved Users
@client.on(events.NewMessage(pattern=r"^\.listapproved$", outgoing=True))
async def list_approved(event):
    if not approved_users:
        return await event.edit("🚫 **No approved users found.**")
    
    approved_list = "\n".join(f"• `{user}`" for user in approved_users)
    await event.edit(f"✅ **Approved users:**\n{approved_list}")

# 🚨 Monitor Unapproved Messages (Fixes applied)
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monitor_unapproved_messages(event):
    global approved_users
    approved_users = load_approved_users()  # Ensure list is updated

    user = event.sender_id

    # Allow messages from approved users
    if user in approved_users:
        return

    # Track unapproved messages
    unapproved_counts[user] = unapproved_counts.get(user, 0) + 1
    msg_count = unapproved_counts[user]

    # First warning message
    if msg_count == 1:
        warning_message = (
            "🌟 **Hello!** 🌟\n\n"
            "You've reached CyberNexus, my assistant! 🚀\n"
            "Please wait while I notify them.\n\n"
            "⚠️ **Note:** Spamming will get you blocked!\n"
            "You can send up to **5 messages** before an automatic block. ✅"
        )
        await event.respond(warning_message)

    # Auto-block after 5 unapproved messages
    if msg_count >= 5:
        try:
            await client(BlockRequest(user))
            await event.respond("🚫 **You have been blocked due to excessive messaging.**")
            unapproved_counts.pop(user, None)  # Reset count
        except Exception:
            pass  # Avoid crashing if block fails
