from telethon import events
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Store approved users & unapproved message counts
approved_users = set()
unapproved_counts = {}

@client.on(events.NewMessage(pattern=r"^\.block( (.*)|$)", outgoing=True))
async def block_user(event):
    """Blocks a user from messaging you."""
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1) or (reply.sender_id if reply else None)
    
    if not user:
        return await event.edit("**Reply to a user or specify their ID to block them.**")
    
    await client(BlockRequest(user))
    if user in approved_users:
        approved_users.remove(user)
    
    await event.edit(f"🚫 **Blocked user:** `{user}`")

@client.on(events.NewMessage(pattern=r"^\.unblock( (.*)|$)", outgoing=True))
async def unblock_user(event):
    """Unblocks a previously blocked user."""
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1) or (reply.sender_id if reply else None)
    
    if not user:
        return await event.edit("**Reply to a user or specify their ID to unblock them.**")
    
    await client(UnblockRequest(user))
    approved_users.add(user)
    await event.edit(f"✅ **Unblocked user:** `{user}`")

@client.on(events.NewMessage(pattern=r"^\.listapproved$", outgoing=True))
async def list_approved(event):
    """Lists all approved users."""
    if not approved_users:
        return await event.edit("🚫 **No approved users found.**")
    
    approved_list = "\n".join(f"• `{user}`" for user in approved_users)
    await event.edit(f"✅ **Approved users:**\n{approved_list}")

@client.on(events.NewMessage(pattern=r"^\.a$", outgoing=True))
async def approve_user(event):
    """Approves a user, allowing them to send messages freely."""
    reply = await event.get_reply_message()
    user = event.sender_id if not reply else reply.sender_id

    if user in approved_users:
        return await event.edit("✅ **User is already approved.**")

    approved_users.add(user)
    await event.edit(f"✅ **Approved user:** `{user}`")

@client.on(events.NewMessage(pattern=r"^\.d$", outgoing=True))
async def disapprove_user(event):
    """Disapproves a user, making them restricted again."""
    reply = await event.get_reply_message()
    user = event.sender_id if not reply else reply.sender_id

    if user in approved_users:
        approved_users.remove(user)
        await event.edit(f"🚫 **User disapproved:** `{user}`")
    else:
        await event.edit("🚫 **User is already unapproved.**")

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monitor_unapproved_messages(event):
    """Handles messages from unapproved users and blocks spammers."""
    user = event.sender_id
    
    # Allow messages from approved users
    if user in approved_users:
        return
    
    # Track the number of messages
    unapproved_counts[user] = unapproved_counts.get(user, 0) + 1

    # Send a warning message only for the first time
    if unapproved_counts[user] == 1:
        warning_message = (
            "👋 **Hey there!**\n\n"
            "You've reached CyberNexus, my owner's personal assistant.\n"
            "I’ve just notified my master about your message—hang tight, a reply is on its way! 🚀\n\n"
            "**⚠ Warning:** Spamming isn't cool—10 messages = instant block! 😬\n"
            "Be patient, and you'll get the attention you deserve. 💬\n\n"
            "× **Powered by CyberNexus**"
        )
        await event.respond(warning_message)

    # Block user after 10 unapproved messages
    if unapproved_counts[user] >= 10:
        await client(BlockRequest(user))
        await event.respond("🚫 **You have been blocked due to sending too many unapproved messages.**")
        del unapproved_counts[user]  # Reset the counter after blocking
