import json
from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# 📜 Help Command
@client.on(events.NewMessage(pattern=r"^\.help_globaltools$", outgoing=True))
async def help_menu(event):
    help_text = """
    **📜 ᴄʏʙᴇʀɴᴇxᴜs ʜᴇʟᴘ ᴍᴇɴᴜ 📜**
    **📝 Available Commands:**
    - `.gcast [message]` 📢 Broadcast
    - `.gucast [message]` 📩 Private broadcast
    """
    await event.edit(help_text)

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
