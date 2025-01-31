from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Dictionary to store warnings
warn_data = {}

# Maximum warnings before auto-action
MAX_WARNINGS = 3

@client.on(events.NewMessage(pattern=r"^\.warn$", outgoing=True))
async def warn_user(event):
    """Warns a user and takes action if they exceed max warnings."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ᴡᴀʀɴ ᴛʜᴇᴍ!**")

    user_id = reply.sender_id
    warn_data[user_id] = warn_data.get(user_id, 0) + 1
    await event.edit(f"**ᴡᴀʀɴᴇᴅ! ⚠️**\nᴛᴏᴛᴀʟ ᴡᴀʀɴɪɴɢs: {warn_data[user_id]}/{MAX_WARNINGS}")

    if warn_data[user_id] >= MAX_WARNINGS:
        await event.reply(f"**ᴜsᴇʀ ʜᴀs ʀᴇᴀᴄʜᴇᴅ {MAX_WARNINGS} ᴡᴀʀɴɪɴɢs! 🚨 ᴀᴜᴛᴏ-ᴀᴄᴛɪᴏɴ ᴛʀɪɢɢᴇʀᴇᴅ.**")
        await client.kick_participant(event.chat_id, user_id)

@client.on(events.NewMessage(pattern=r"^\.resetwarn$", outgoing=True))
async def reset_warn(event):
    """Resets warnings for a user."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ʀᴇsᴇᴛ ᴛʜᴇɪʀ ᴡᴀʀɴɪɴɢs!**")

    user_id = reply.sender_id
    warn_data.pop(user_id, None)
    await event.edit("**ᴡᴀʀɴɪɴɢs ʀᴇsᴇᴛ! ✅**")

@client.on(events.NewMessage(pattern=r"^\.warns$", outgoing=True))
async def show_warns(event):
    """Shows the number of warnings a user has."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇɪʀ ᴡᴀʀɴɪɴɢs!**")

    user_id = reply.sender_id
    warnings = warn_data.get(user_id, 0)
    await event.edit(f"**ᴜsᴇʀ ʜᴀs {warnings}/{MAX_WARNINGS} ᴡᴀʀɴɪɴɢs.**")

@client.on(events.NewMessage(pattern=r"^\.setwarn (\d+)$", outgoing=True))
async def set_warn_limit(event):
    """Sets the max warning limit before auto-action."""
    global MAX_WARNINGS
    arg = event.pattern_match.group(1)

    try:
        MAX_WARNINGS = int(arg)
        await event.edit(f"**ᴍᴀx ᴡᴀʀɴɪɴɢs sᴇᴛ ᴛᴏ {MAX_WARNINGS}! ✅**")
    except ValueError:
        await event.edit("**ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ! ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ ᴛᴏ sᴇᴛ ᴡᴀʀɴɪɴɢs.**")

@client.on(events.NewMessage(pattern=r"^\.warnhelp$", outgoing=True))
async def warn_help(event):
    """Displays help for warning commands."""
    help_text = (
        "**🚨 ᴡᴀʀɴ ᴘʟᴜɢɪɴ ʜᴇʟᴘ 🚨**\n\n"
        "`.warn` - ᴡᴀʀɴ ᴀ ᴜsᴇʀ (ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ).\n"
        "`.resetwarn` - ʀᴇsᴇᴛ ᴡᴀʀɴɪɴɢs ᴏғ ᴀ ᴜsᴇʀ.\n"
        "`.warns` - ᴄʜᴇᴄᴋ ᴡᴀʀɴɪɴɢ ᴄᴏᴜɴᴛ ᴏғ ᴀ ᴜsᴇʀ.\n"
        "`.setwarn <ɴᴜᴍʙᴇʀ>` - sᴇᴛ ᴍᴀx ᴡᴀʀɴɪɴɢs ʙᴇғᴏʀᴇ ᴀᴜᴛᴏ-ᴀᴄᴛɪᴏɴ.\n"
    )
    await event.edit(help_text)
