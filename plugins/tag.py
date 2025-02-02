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


@client.on(events.NewMessage(pattern=r"^\.help_tag$", outgoing=True))
async def help_tag(event):
    """Displays detailed help for the .tag command."""
    help_tag_message = (
        "✵ **ᴅᴇᴛᴀɪʟᴇᴅ ʜᴇʟᴘ ғᴏʀ .ᴛᴀɢ** ✵\n\n"
        "The `.tag` command allows you to tag users in the group based on different criteria.\n\n"
        "• `.tag on` – Enables tagging members in the group.\n"
        "• `.tag off` – Disables tagging.\n"
        "• `.tag all` – Tags all users in the group (when enabled).\n"
        "• `.tag bots` – Tags all bots in the group (when enabled).\n"
        "• `.tag admins` – Tags all admins in the group (when enabled).\n"
        "• `.tag owner` – Tags the owner of the group (when enabled).\n\n"
        "Tagging components can be enabled or disabled with `.tag on` and `.tag off` commands."
    )
    await event.edit(help_tag_message)


async def tag_all_users(event):
    """Tags all users in the group."""
    participants = await client.get_participants(event.chat_id)
    mentions = " ".join([f"[{user.username or user.first_name}](tg://user?id={user.id})" for user in participants])
    await event.reply(f"**Tagging All Users:**\n{mentions}")


async def tag_bots(event):
    """Tags all bots in the group."""
    participants = await client.get_participants(event.chat_id, filter=telethon.tl.types.ChannelParticipantsBots)
    mentions = " ".join([f"[{bot.username or bot.first_name}](tg://user?id={bot.id})" for bot in participants])
    await event.reply(f"**Tagging Bots:**\n{mentions}")


async def tag_admins(event):
    """Tags all admins in the group."""
    participants = await client.get_participants(event.chat_id, filter=telethon.tl.types.ChannelParticipantsAdmins)
    mentions = " ".join([f"[{admin.username or admin.first_name}](tg://user?id={admin.id})" for admin in participants])
    await event.reply(f"**Tagging Admins:**\n{mentions}")


async def tag_owner(event):
    """Tags the owner of the group."""
    owner = await client.get_entity(event.chat_id)
    owner_mention = f"[{owner.username or owner.first_name}](tg://user?id={owner.id})"
    await event.reply(f"**Tagging Owner:**\n{owner_mention}")
