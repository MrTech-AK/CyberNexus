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

# Admin commands and their functionalities

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

# Kick and ban user commands

@client.on(events.NewMessage(pattern=r"^\.kick$", outgoing=True))
async def kick_user(event):
    """Kicks a user from the group."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ᴋɪᴄᴋ ᴛʜᴇᴍ!**")

    user_id = reply.sender_id
    await client.kick_participant(event.chat_id, user_id)
    await event.edit("**ᴜsᴇʀ ᴋɪᴄᴋᴇᴅ! 🚫**")

@client.on(events.NewMessage(pattern=r"^\.ban$", outgoing=True))
async def ban_user(event):
    """Bans a user from the group."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ʙᴀɴ ᴛʜᴇᴍ!**")

    user_id = reply.sender_id
    await client.ban_participant(event.chat_id, user_id)
    await event.edit("**ᴜsᴇʀ ʙᴀɴɴᴇᴅ! 🚫**")

@client.on(events.NewMessage(pattern=r"^\.unban$", outgoing=True))
async def unban_user(event):
    """Unbans a user from the group."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ᴜɴʙᴀɴ ᴛʜᴇᴍ!**")

    user_id = reply.sender_id
    await client.unban_participant(event.chat_id, user_id)
    await event.edit("**ᴜsᴇʀ ᴜɴʙᴀɴɴᴇᴅ! ✅**")

# VC start and end commands

@client.on(events.NewMessage(pattern=r"^\.vc_start$", outgoing=True))
async def vc_start(event):
    """Starts a voice chat in the group."""
    await client.send_message(event.chat_id, "/startvc")  # This may depend on the group bot's command or feature
    await event.edit("**🎤 Vᴏɪᴄᴇ ᴄʜᴀᴛ ᴅᴇᴘᴀʀᴛᴇᴅ! 🎧**")

@client.on(events.NewMessage(pattern=r"^\.vc_end$", outgoing=True))
async def vc_end(event):
    """Ends a voice chat in the group."""
    await client.send_message(event.chat_id, "/endvc")  # This may depend on the group bot's command or feature
    await event.edit("**🎤 Vᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ! ❌**")

# Pin message command

@client.on(events.NewMessage(pattern=r"^\.pin$", outgoing=True))
async def pin_message(event):
    """Pins a message."""
    reply = await event.get_reply_message()
    if not reply:
        return await event.edit("**ᴇʀʀᴏʀ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ ɪᴛ!**")
    
    await reply.pin()
    await event.edit("**📌 ᴍᴇssᴀɢᴇ ᴘɪɴɴᴇᴅ!**")

# Display admin tools help

@client.on(events.NewMessage(pattern=r"^\.admintoolshelp$", outgoing=True))
async def admin_tools_help(event):
    """Displays help for all admin tools."""
    help_message = (
        "**👑 ᴀᴅᴍɪɴ ᴛᴏᴏʟs ʜᴇʟᴘ 👑**\n\n"
        "• `.warn` – Warn a user (reply to a message to warn the user).\n"
        "• `.resetwarn` – Reset warnings for a user.\n"
        "• `.warns` – Check the warning count of a user.\n"
        "• `.setwarn <number>` – Set the max warning count before auto-action.\n"
        "• `.kick` – Kick a user from the group (reply to their message).\n"
        "• `.ban` – Ban a user from the group (reply to their message).\n"
        "• `.unban` – Unban a user from the group (reply to their message).\n"
        "• `.vc_start` – Start a voice chat.\n"
        "• `.vc_end` – End a voice chat.\n"
        "• `.pin` – Pin a message.\n\n"
        "For more info, use `.warnhelp` or `.kickhelp` etc."
    )
    await event.edit(help_message)

# Help command for warning system

@client.on(events.NewMessage(pattern=r"^\.warnhelp$", outgoing=True))
async def warn_help(event):
    """Displays help for warning commands."""
    help_text = (
        "**🚨 ᴡᴀʀɴ ᴘʟᴜɢɪɴ ʜᴇʟᴘ 🚨**\n\n"
        "`.warn` - ᴡᴀʀɴ ᴀ ᴜsᴇʀ (ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ).\n"
        "`.resetwarn` - ʀᴇsᴇᴛ ᴡᴀʀɴɪɴɢs ᴏғ ᴀ ᴜsᴇʀ.\n"
        "`.warns` - ᴄʜᴇᴄᴋ ᴡᴀʀɴɪɴɢ ᴄᴏᴜɴᴛ ᴏғ ᴀ ᴜsᴇʀ.\n"
        "`.setwarn <number>` - ᴄᴏɴꜰɪɢᴜʀᴇ ᴛʜᴇ ᴍᴀx ᴡᴀʀɴɪɴɢs ᴀ ᴜsᴇʀ ᴄᴀɴ ʜᴀᴠᴇ.\n"
        "For more information, use `.admintoolshelp` to get a list of all admin commands."
    )
    await event.edit(help_text)

# Help command for kick/ban system
@client.on(events.NewMessage(pattern=r"^\.kickhelp$", outgoing=True))
async def kick_help(event):
    """Displays help for kick/ban commands."""
    help_text = (
        "**🚫 ᴋɪᴄᴋ/ʙᴀɴ ʜᴇʟᴘ 🚫**\n\n"
        "`.kick` - ᴋɪᴄᴋ ᴀ ᴜsᴇʀ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇɪʀ ᴍᴇssᴀɢᴇ.\n"
        "`.ban` - ʙᴀɴ ᴀ ᴜsᴇʀ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇɪʀ ᴍᴇssᴀɢᴇ.\n"
        "`.unban` - ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇɪʀ ᴍᴇssᴀɢᴇ."
    )
    await event.edit(help_text)

# Initialize the client
if __name__ == "__main__":
    client.run_until_disconnected()
