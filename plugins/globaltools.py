import json
from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Load banned users from file
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

# 📜 Help Command
@client.on(events.NewMessage(pattern=r"^\.help_globaltools$", outgoing=True))
async def help_menu(event):
    help_text = """
    **📜 ᴄʏʙᴇʀɴᴇxᴜs ʜᴇʟᴘ ᴍᴇɴᴜ 📜**
    **📝 Available Commands:**
    - `.gban [user]` 🚫 Ban globally
    - `.ungban [user]` ✅ Unban globally
    - `.gkick [user]` 🦵 Kick globally
    - `.gmute [user]` 🔇 Mute globally
    - `.ungmute [user]` 🔊 Unmute globally
    - `.gpromote [user]` 🌟 Promote globally
    - `.gdemote [user]` 👎 Demote globally
    - `.gcast [message]` 📢 Broadcast
    - `.gucast [message]` 📩 Private broadcast
    - `.listgban` 🔍 List banned users
    """
    await event.edit(help_text)

# 🚫 **Global Ban**
@client.on(events.NewMessage(pattern=r"^\.gban(?: (.*))?$", outgoing=True))
async def gban(event):
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1) or (reply.sender_id if reply else None)

    if not user:
        return await event.edit("⚠️ **Reply to a user or provide an ID to ban.**")

    user = str(user)
    if user not in global_banned_users:
        global_banned_users.append(user)
        save_banned_users()
        await event.edit(f"🚫 **User `{user}` has been globally banned.**")
        
        # Ban user in all groups
        async for chat in client.iter_dialogs():
            try:
                await client.edit_permissions(chat.id, user, view_messages=False)
            except Exception as e:
                print(f"Error banning in {chat.id}: {e}")

# ✅ **Global Unban**
@client.on(events.NewMessage(pattern=r"^\.ungban(?: (.*))?$", outgoing=True))
async def ungban(event):
    reply = await event.get_reply_message()
    user = event.pattern_match.group(1) or (reply.sender_id if reply else None)

    if not user:
        return await event.edit("⚠️ **Reply to a user or provide an ID to unban.**")

    user = str(user)
    if user in global_banned_users:
        global_banned_users.remove(user)
        save_banned_users()
        await event.edit(f"✅ **User `{user}` has been globally unbanned.**")
        
        # Unban user in all groups
        async for chat in client.iter_dialogs():
            try:
                await client.edit_permissions(chat.id, user, view_messages=True)
            except Exception as e:
                print(f"Error unbanning in {chat.id}: {e}")

# 🔍 **List Globally Banned Users**
@client.on(events.NewMessage(pattern=r"^\.listgban$", outgoing=True))
async def listgban(event):
    if not global_banned_users:
        return await event.edit("🚫 **No users are globally banned.**")
    user_list = "\n".join(f"• `{user}`" for user in global_banned_users)
    await event.edit(f"🔍 **Globally Banned Users:**\n{user_list}")

# 🌟 **Global Promote**
@client.on(events.NewMessage(pattern=r"^\.gpromote(?: (.*))?$", outgoing=True))
async def gpromote(event):
    user = event.pattern_match.group(1) or event.sender_id
    async for chat in client.iter_dialogs():
        try:
            await client.edit_admin(chat.id, user, is_admin=True)
        except Exception as e:
            print(f"Error promoting in {chat.id}: {e}")
    await event.edit(f"🌟 **User `{user}` has been globally promoted!** 🎉")

# 👎 **Global Demote**
@client.on(events.NewMessage(pattern=r"^\.gdemote(?: (.*))?$", outgoing=True))
async def gdemote(event):
    user = event.pattern_match.group(1) or event.sender_id
    async for chat in client.iter_dialogs():
        try:
            await client.edit_admin(chat.id, user, is_admin=False)
        except Exception as e:
            print(f"Error demoting in {chat.id}: {e}")
    await event.edit(f"👎 **User `{user}` has been globally demoted.** 😔")

# 🦵 **Global Kick**
@client.on(events.NewMessage(pattern=r"^\.gkick(?: (.*))?$", outgoing=True))
async def gkick(event):
    user = event.pattern_match.group(1) or event.sender_id
    async for chat in client.iter_dialogs():
        try:
            await client.kick_participant(chat.id, user)
        except Exception as e:
            print(f"Error kicking in {chat.id}: {e}")
    await event.edit(f"🦵 **User `{user}` has been globally kicked.** 🚶‍♂️")

# 🔇 **Global Mute**
@client.on(events.NewMessage(pattern=r"^\.gmute(?: (.*))?$", outgoing=True))
async def gmute(event):
    user = event.pattern_match.group(1) or event.sender_id
    async for chat in client.iter_dialogs():
        try:
            await client.edit_permissions(chat.id, user, send_messages=False)
        except Exception as e:
            print(f"Error muting in {chat.id}: {e}")
    await event.edit(f"🔇 **User `{user}` has been globally muted.** 🔕")

# 🔊 **Global Unmute**
@client.on(events.NewMessage(pattern=r"^\.ungmute(?: (.*))?$", outgoing=True))
async def ungmute(event):
    user = event.pattern_match.group(1) or event.sender_id
    async for chat in client.iter_dialogs():
        try:
            await client.edit_permissions(chat.id, user, send_messages=True)
        except Exception as e:
            print(f"Error unmuting in {chat.id}: {e}")
    await event.edit(f"🔊 **User `{user}` has been globally unmuted.** 🗣️")

# 📢 **Global Broadcast**
@client.on(events.NewMessage(pattern=r"^\.gcast (.+)", outgoing=True))
async def gcast(event):
    message = event.pattern_match.group(1)
    async for chat in client.iter_dialogs():
        try:
            await client.send_message(chat.id, message)
        except Exception as e:
            print(f"Error broadcasting to {chat.id}: {e}")
    await event.edit("📢 **Message sent to all groups!**")

# 📩 **Global Private Broadcast**
@client.on(events.NewMessage(pattern=r"^\.gucast (.+)", outgoing=True))
async def gucast(event):
    message = event.pattern_match.group(1)
    async for chat in client.iter_dialogs():
        if chat.is_user:
            try:
                await client.send_message(chat.id, message)
            except Exception as e:
                print(f"Error sending private message to {chat.id}: {e}")
    await event.edit("📩 **Message sent to all private chats!**")
