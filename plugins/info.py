from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from datetime import datetime
from cybernexus import client
import platform 

@client.on(events.NewMessage(pattern=r"^\.info(?:\s+(.+))?$", outgoing=True))
async def user_info(event):
    """Fetches and displays full user info."""
    input_arg = event.pattern_match.group(1)

    # Determine the target user (replied user, mentioned username, or user ID)
    if event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        user = await client(GetFullUserRequest(replied_msg.sender_id))
    elif input_arg:
        user = await client(GetFullUserRequest(input_arg))
    else:
        return await event.edit("❌ **Reply to a user or provide a username/user ID!**")

    user_data = user.users[0]  # ✅ Corrected way to access user details

    # Extract details safely
    full_name = f"{user_data.first_name or ''} {user_data.last_name or ''}".strip()
    username = f"@{user_data.username}" if user_data.username else "None"
    user_id = user_data.id
    profile_link = f"[Click Here](tg://user?id={user_id})"
    
    # Format the response
    info_text = (
        "✨ **User Info** ✨\n\n"
        f"👤 **Full Name:** {full_name}\n"
        f"🔹 **Username:** {username}\n"
        f"🆔 **User ID:** `{user_id}`\n"
        f"🌍 **Profile Link:** {profile_link}\n\n"
        "⚡ Powered by CyberNexus"
    )

    await event.edit(info_text)
