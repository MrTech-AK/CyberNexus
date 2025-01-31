from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Store approved users
approved_users = []

@client.on(events.NewMessage(pattern=r"^\.block( (.*)|$)", outgoing=True))
async def block_user(event):
    """Blocks the specified user from sending you messages."""
    if event.pattern_match.group(1):
        user = event.pattern_match.group(1)
    else:
        user = event.sender_id
    
    if user not in approved_users:
        approved_users.append(user)
        await event.edit(f"**User {user} has been blocked.**")
    else:
        await event.edit("**User is already blocked.**")

@client.on(events.NewMessage(pattern=r"^\.unblock( (.*)|$)", outgoing=True))
async def unblock_user(event):
    """Unblocks the specified user."""
    if event.pattern_match.group(1):
        user = event.pattern_match.group(1)
    else:
        user = event.sender_id
    
    if user in approved_users:
        approved_users.remove(user)
        await event.edit(f"**User {user} has been unblocked.**")
    else:
        await event.edit("**User is not blocked.**")

@client.on(events.NewMessage(pattern=r"^\.listapproved$", outgoing=True))
async def list_approved(event):
    """Lists all approved users."""
    if approved_users:
        approved_list = "\n".join(str(user) for user in approved_users)
        await event.edit(f"**Approved users:**\n{approved_list}")
    else:
        await event.edit("**No approved users found.**")

@client.on(events.NewMessage(pattern=r"^\.a$", outgoing=True))
async def approve_user(event):
    """Approves the sender to send messages without being blocked."""
    user = event.sender_id
    if user not in approved_users:
        approved_users.append(user)
        await event.edit(f"**User {user} has been approved.**")
    else:
        await event.edit("**User is already approved.**")

@client.on(events.NewMessage(pattern=r"^\.d$", outgoing=True))
async def disapprove_user(event):
    """Disapproves a user, blocking them after 10 messages."""
    user = event.sender_id
    if user not in approved_users:
        approved_users.append(user)
        await event.edit(f"**User {user} has been disapproved. They will be blocked after 10 unapproved messages.**")
    else:
        await event.edit("**User is already disapproved.**")

# Function to send the custom message when an unapproved user sends a message
@client.on(events.NewMessage(incoming=True))
async def monitor_unapproved_messages(event):
    if event.sender_id not in approved_users:
        # Send a greeting message to unapproved users
        greeting_message = (
            "Hey there! 👋\n\n"
            "You've reached CyberNexus, the personal assistant of my awesome master.\n"
            "I’ve just notified my master about your message—hang tight, a reply is on its way! 🚀\n\n"
            "But a quick heads-up: Spamming isn't cool—10 messages = instant block! 😬\n"
            "Be patient, and you'll get the attention you deserve. 💬\n\n"
            "× Powered by CyberNexus"
        )
        await event.respond(greeting_message)

        # Track unapproved messages
        if hasattr(event.sender_id, 'unapproved_messages'):
            event.sender_id.unapproved_messages += 1
        else:
            event.sender_id.unapproved_messages = 1
        
        # Auto-block user after 10 unapproved messages
        if event.sender_id.unapproved_messages >= 10:
            await client.send_message(event.sender_id, "You have been blocked due to sending 10 unapproved messages.")
            await client.block_user(event.sender_id)
            await event.respond("**User has been blocked due to sending 10 unapproved messages.**")
            del event.sender_id.unapproved_messages  # Reset the counter after blocking
