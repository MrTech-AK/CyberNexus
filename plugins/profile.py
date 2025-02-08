from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
from telethon.tl.functions.account import UpdateProfileRequest, UpdateProfilePhotoRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import platform 
@client.on(events.NewMessage(pattern=r"^\.setbio (.*)", outgoing=True))
async def set_bio(event):
    """Sets the bio of the user."""
    bio = event.pattern_match.group(1)
    try:
        await client(UpdateProfileRequest(about=bio))
        await event.edit(f"**Your bio has been updated to:**\n{bio}")
    except Exception as e:
        await event.edit(f"**Error updating bio:**\n{str(e)}")

@client.on(events.NewMessage(pattern=r"^\.setname (.*)", outgoing=True))
async def set_name(event):
    """Sets the name of the user."""
    name = event.pattern_match.group(1)
    try:
        await client(UpdateProfileRequest(first_name=name))
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
            uploaded_photo = await client.upload_file(photo)
            await client(UpdateProfilePhotoRequest(uploaded_photo))
            await event.edit("**Your profile picture has been updated.**")
        except Exception as e:
            await event.edit(f"**Error updating profile picture:**\n{str(e)}")
    else:
        await event.edit("**Please reply to a photo to set it as your profile picture.**")

@client.on(events.NewMessage(pattern=r"^\.delpfp$", outgoing=True))
async def del_pfp(event):
    """Deletes the profile picture of the user."""
    try:
        photos = await client.get_profile_photos("me", limit=1)
        if photos:
            await client(DeletePhotosRequest(photos))
            await event.edit("**Your profile picture has been deleted.**")
        else:
            await event.edit("**You don't have a profile picture set.**")
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
        "• `.setbio <text>` – Change your bio.\n"
        "    Example: `.setbio I am using CyberNexus Userbot!`\n\n"
        "• `.setname <name>` – Change your name.\n"
        "    Example: `.setname John Doe`\n\n"
        "• `.setpic` – Change your profile picture by replying to a photo.\n\n"
        "• `.delpfp` – Delete your profile picture.\n\n"
        "• `.poto` – Show your current profile picture."
    )
    await event.edit(help_message)
