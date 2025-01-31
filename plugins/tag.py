from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# To store the status of tagging
tag_status = {
    "on": False,
    "off": True,
    "all": False,
    "bots": False,
    "rec": False,
    "admins": False,
    "owner": False
}

@client.on(events.NewMessage(pattern=r"^\.tag (on|off|all|bots|rec|admins|owner)$", outgoing=True))
async def tag_command(event):
    """Handles the tagging commands."""
    tag_type = event.pattern_match.group(1).lower()

    if tag_type not in tag_status:
        return await event.edit("**ᴇʀʀᴏʀ: ɪɴᴠᴀʟɪᴅ ᴛᴀɢ ᴏᴘᴛɪᴏɴ!**")

    # Toggle the tag status
    tag_status[tag_type] = not tag_status[tag_type]
    status = "ᴏɴ" if tag_status[tag_type] else "ᴏғғ"

    if tag_type == "all" and tag_status["all"]:
        await tag_all_users(event)
    elif tag_type == "bots" and tag_status["bots"]:
        await tag_bots(event)
    elif tag_type == "admins" and tag_status["admins"]:
        await tag_admins(event)
    elif tag_type == "owner" and tag_status["owner"]:
        await tag_owner(event)

    await event.edit(f"**ᴛᴀɢɢɪɴɢ ᴄᴏᴍᴘᴏɴᴇɴᴛ {tag_type} ɪs ɴᴏᴡ {status}**")

@client.on(events.NewMessage(pattern=r"^\.taghelp$", outgoing=True))
async def tag_help(event):
    """Displays help for the .tag command."""
    help_message = (
        "✵ **ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ .ᴛᴀɢ** ✵\n\n"
        "• `.tag on` – ᴇɴᴀʙʟᴇ ᴛᴀɢɢɪɴɢ ᴍᴇᴍʙᴇʀs\n"
        "• `.tag off` – ᴅɪsᴀʙʟᴇ ᴛᴀɢɢɪɴɢ\n"
        "• `.tag all` – ᴛᴀɢs ᴀʟʟ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
        "• `.tag bots` – ᴛᴀɢs ᴀʟʟ ʙᴏᴛs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
        "• `.tag admins` – ᴛᴀɢs ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
        "• `.tag owner` – ᴛᴀɢs ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ\n\n"
        "ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴇɴᴀʙʟᴇᴅ ᴏʀ ᴅɪsᴀʙʟᴇᴅ ᴏɴᴄᴇ ᴡɪᴛʜ `.tag on` ᴀɴᴅ `.tag off`."
    )
    await event.edit(help_message)
