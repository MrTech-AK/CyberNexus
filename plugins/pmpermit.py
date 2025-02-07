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

# Load approved users from file safely
def load_approved_users():
    if os.path.exists(APPROVED_USERS_FILE):
        try:
            with open(APPROVED_USERS_FILE, "r") as f:
                return set(json.load(f))
        except json.JSONDecodeError:
            return set()  # If JSON is corrupted, reset it
    return set()

approved_users = load_approved_users()
unapproved_counts = {}

# Function to save approved users
def save_approved_users():
    with open(APPROVED_USERS_FILE, "w") as f:
        json.dump(list(approved_users), f)

# 📚 Help Command
@client.on(events.NewMessage(pattern=r"^\.help_pmpermit$", outgoing=True))
async def pmpermit_help(event):
    """Sends a help message explaining how to get approved and the rules."""
    help_message = (
        "📚 **PM Permit Help** 📚\n\n"
        "Welcome to CyberNexus! Here's how to interact with me:\n\n"
        "1. **Approve a user**: Use `.a` to approve a user and allow them to send messages freely.\n"
        "2. **Disapprove a user**: Use `.da` to disapprove a user and restrict them from messaging.\n"
        "3. **Block a user**: Use `.block <user_id>` to block a user from messaging you.\n"
        "4. **Unblock a user**: Use `.unblock <user_id>` to unblock a previously blocked user.\n"
        "5. **List approved users**: Use `.listapproved` to see all approved users.\n"
        "6. **Unapproved messages**: Any unapproved user can send up to **5 messages** before getting blocked automatically.\n\n"
        "🛑 **Important**: Spamming isn't cool! 🚫 5 messages = Instant block!\n\n"
        "💡 **Pro Tip**: Be patient and stay cool—your message is important! 😎"
    )
    await event.edit(help_message)

# ✅ Approve a User
@client.on(events.NewMessage(pattern=r"^\.a$", outgoing=True))
async def approve_user(event):
    """Approves a user, allowing them to send messages freely."""
    reply = await event.get_reply_message()
    user = reply.sender_id if reply else event.sender_id

    if user in approved_users:
        return await event.edit("✅ **User is already approved.**")

    approved_users.add(user)
    save_approved_users()

    # Reload approved users to ensure changes take effect immediately
    global approved_users
    approved_users = load_approved_users()

    await event.edit(f"✅ **Approved user:** `{user}`")


# 🚫 Disapprove a User
@client.on(events.NewMessage(pattern=r"^\.da$", outgoing=True))
async def disapprove_user(event):
    """Disapproves a user, making them restricted again."""
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
    """Blocks a user from messaging you."""
    reply = await event.get_reply_message()
    user = event.pattern_match.group(2) or (reply.sender_id if reply else None)
    
    if not user:
        return await event.edit("**Reply to a user or specify their ID to block them.**")
    
    try:
        user = int(user)  # Ensure user ID is an integer
    except ValueError:
        return await event.edit("❌ **Invalid user ID!**")

    await client(BlockRequest(user))
    approved_users.discard(user)  # Use discard to avoid KeyError
    save_approved_users()

    await event.edit(f"🚫 **Blocked user:** `{user}`")

# ✅ Unblock a User
@client.on(events.NewMessage(pattern=r"^\.unblock( (.*)|$)", outgoing=True))
async def unblock_user(event):
    """Unblocks a previously blocked user."""
    reply = await event.get_reply_message()
    user = event.pattern_match.group(2) or (reply.sender_id if reply else None)
    
    if not user:
        return await event.edit("**Reply to a user or specify their ID to unblock them.**")
    
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
    """Lists all approved users."""
    if not approved_users:
        return await event.edit("🚫 **No approved users found.**")
    
    approved_list = "\n".join(f"• `{user}`" for user in approved_users)
    await event.edit(f"✅ **Approved users:**\n{approved_list}")

# 🚨 Monitor Unapproved Messages
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monitor_unapproved_messages(event):
    """Handles messages from unapproved users and blocks spammers."""
    global approved_users
    approved_users = load_approved_users()  # Reload approved users

    user = event.sender_id

    # Allow messages from approved users
    if user in approved_users:
        return

    # Track the number of messages for unapproved users
    if user not in unapproved_counts:
        unapproved_counts[user] = 1
    else:
        unapproved_counts[user] += 1

    msg_count = unapproved_counts[user]

    # Send a warning message with a dynamic message count
    if msg_count <= 5:
        warning_message = (
            "🌟 Hey there! 🌟\n\n"
            "You've just connected with CyberNexus, the personal assistant of my owner! ✨\n"
            "I'm notifying them right now, so hang tight—your reply is coming soon! 🚀\n"
            "Keep it chill, and you'll get the attention you deserve! 💬\n\n"
            "× Powered by CyberNexus 💻"
        )
        await event.respond(warning_message)

    # Block user after 5 unapproved messages
    if msg_count >= 5:
        await client(BlockRequest(user))
        await event.respond("🚫 **You have been blocked due to sending too many unapproved messages.**")
        del unapproved_counts[user]  # Reset the counter after blocking
