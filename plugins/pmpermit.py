import os
import json
import config
import time
import sys
import telethon
import platform
from telethon import events
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from cybernexus import client

# 🔹 Storage files
APPROVED_USERS_FILE = "approved_users.json"
WARNINGS_FILE = "warnings.json"

# 🔹 Load Approved Users
if os.path.exists(APPROVED_USERS_FILE):
    with open(APPROVED_USERS_FILE, "r") as file:
        APPROVED_USERS = json.load(file)
else:
    APPROVED_USERS = []

# 🔹 Load Warning Counts
if os.path.exists(WARNINGS_FILE):
    with open(WARNINGS_FILE, "r") as file:
        WARNINGS = json.load(file)
else:
    WARNINGS = {}

# 🔹 Auto-reply and warning system
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private and e.sender_id not in APPROVED_USERS))
async def pm_permit(event):
    user_id = str(event.sender_id)

    # Ignore if already blocked
    if WARNINGS.get(user_id, 0) >= 5:
        return

    # Increment warnings
    WARNINGS[user_id] = WARNINGS.get(user_id, 0) + 1

    # Save updated warnings
    with open(WARNINGS_FILE, "w") as file:
        json.dump(WARNINGS, file)

    # Send warning message
    warning_no = WARNINGS[user_id]
    message = f"""
🌟 **Hey there!** 🌟

You've just connected with **CyberNexus**, the personal assistant of my owner! ✨  
I'm notifying them right now, so hang tight—your reply is coming soon! 🚀

⚠️ **Warning:** No spamming, please! 🚫 ({warning_no}/5)  
After **5 messages**, you will be blocked automatically! 😬  
Keep it chill, and you'll get the attention you deserve! 💬  

💡 **Pro Tip:** Patience pays off, and your message is worth it. 😎  

× **Powered by CyberNexus** 💻
"""
    await event.reply(message)

    # Auto-block after 5 warnings
    if WARNINGS[user_id] >= 5:
        await client(BlockRequest(event.sender_id))
        await event.respond("**🚫 You have been blocked due to excessive messaging!**")

# 🔹 Approve user (.ap)
@client.on(events.NewMessage(pattern=r"^\.ap$", outgoing=True))
async def approve_user(event):
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user_id = str(replied_msg.sender_id)

        if user_id not in APPROVED_USERS:
            APPROVED_USERS.append(user_id)
            with open(APPROVED_USERS_FILE, "w") as file:
                json.dump(APPROVED_USERS, file)

            WARNINGS.pop(user_id, None)  # Reset warnings
            with open(WARNINGS_FILE, "w") as file:
                json.dump(WARNINGS, file)

            await event.reply(f"✅ **User {replied_msg.sender.first_name} has been approved!**")
        else:
            await event.reply("✅ **User is already approved.**")
    else:
        await event.reply("⚠ **Reply to a message to approve the user!**")

# 🔹 Disapprove user (.da)
@client.on(events.NewMessage(pattern=r"^\.da$", outgoing=True))
async def disapprove_user(event):
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user_id = str(replied_msg.sender_id)

        if user_id in APPROVED_USERS:
            APPROVED_USERS.remove(user_id)
            with open(APPROVED_USERS_FILE, "w") as file:
                json.dump(APPROVED_USERS, file)

            WARNINGS[user_id] = 0  # Reset warnings
            with open(WARNINGS_FILE, "w") as file:
                json.dump(WARNINGS, file)

            await event.reply(f"🚫 **User {replied_msg.sender.first_name} has been disapproved!**")
        else:
            await event.reply("⚠ **User is not approved yet.**")
    else:
        await event.reply("⚠ **Reply to a message to disapprove the user!**")

# 🔹 Block user (.block)
@client.on(events.NewMessage(pattern=r"^\.block$", outgoing=True))
async def block_user(event):
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id

        await client(BlockRequest(user_id))
        await event.reply(f"🚫 **User {replied_msg.sender.first_name} has been blocked!**")
    else:
        await event.reply("⚠ **Reply to a message to block the user!**")

# 🔹 Unblock user (.unblock)
@client.on(events.NewMessage(pattern=r"^\.unblock$", outgoing=True))
async def unblock_user(event):
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id

        await client(UnblockRequest(user_id))
        await event.reply(f"✅ **User {replied_msg.sender.first_name} has been unblocked!**")
    else:
        await event.reply("⚠ **Reply to a message to unblock the user!**")
