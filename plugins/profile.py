from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.setbio (.*)", outgoing=True))
async def set_bio(event):
    """Sets the bio of the user."""
    bio = event.pattern_match.group(1)
    try:
        await client.update_profile(bio=bio)
        await event.edit(f"**Your bio has been updated to:**\n{bio}")
    except Exception as e:
        await event.edit(f"**Error updating bio:**\n{str(e)}")


@client.on(events.NewMessage(pattern=r"^\.setname (.*)", outgoing=True))
async def set_name(event):
    """Sets the name of the user."""
    name = event.pattern_match.group(1)
    try:
        await client.update_profile(first_name=name)
        await event.edit(f"**Your name has been updated to:**\n{name}")
    except Exception as e:
        await event.edit(f"**Error updating name:**\n{str(e)}")


@client.on(events.NewMessage(pattern=r"^\.setpic$", outgoing=True))
async def set_pic(event):
    """Sets the profile picture of the user."""
    if event.reply_to_msg_id:
        message = await event.get_reply_message()
        photo = await message.download_media()
        try:
            await client.update_profile(photo=photo)
            await event.edit("**Your profile picture has been updated.**")
        except Exception as e:
            await event.edit(f"**Error updating profile picture:**\n{str(e)}")
    else:
        await event.edit("**Please reply to a photo to set it as your profile picture.**")


@client.on(events.NewMessage(pattern=r"^\.delpfp$", outgoing=True))
async def del_pfp(event):
    """Deletes the profile picture of the user."""
    try:
        await client.update_profile(photo=None)
        await event.edit("**Your profile picture has been deleted.**")
    except Exception as e:
        await event.edit(f"**Error deleting profile picture:**\n{str(e)}")


@client.on(events.NewMessage(pattern=r"^\.poto$", outgoing=True))
async def poto(event):
    """Sends the current profile picture of the user."""
    try:
        profile = await client.get_profile_photos("me", limit=1)
        if profile:
            await client.send_file(event.chat_id, profile[0])
        else:
            await event.edit("**You don't have a profile picture set.**")
    except Exception as e:
        await event.edit(f"**Error retrieving profile picture:**\n{str(e)}")


@client.on(events.NewMessage(pattern=r"^\.profilehelp$", outgoing=True))
async def profile_help(event):
    """Displays help for profile-related commands."""
    help_message = (
        "✵ **Profile Commands** ✵\n\n"
        "• `.setbio <text>` – ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʙɪᴏ ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ᴛᴇxᴛ.\n"
        "    Example: `.setbio I am using CyberNexus Userbot!`\n\n"
        "• `.setname <name>` – ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ɴᴀᴍᴇ ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɴᴀᴍᴇ.\n"
        "    Example: `.setname John Doe`\n\n"
        "• `.setpic` – ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ.\n\n"
        "• `.delpfp` – ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ.\n\n"
        "• `.poto` – ᴛᴇʟʟs ʏᴏᴜ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ."
    )
    await event.edit(help_message)
