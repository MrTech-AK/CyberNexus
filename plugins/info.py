from telethon import events
from cybernexus import client
from telethon.tl.functions.users import GetFullUserRequest
from datetime import datetime

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
        await event.edit("**Reply to a user or provide a username/user ID!**")
        return

    user_info = user.user

    # Extract details
    full_name = f"{user_info.first_name or ''} {user_info.last_name or ''}".strip()
    username = f"@{user_info.username}" if user_info.username else "None"
    user_id = user_info.id
    profile_link = f"[Click Here](tg://user?id={user_id})"
    account_creation_date = datetime.fromtimestamp(user_info.date.timestamp()).strftime("%d %B %Y")
    status = "Premium User" if user_info.premium else "Regular User"
    bio = user.about if user.about else "No bio set."

    # Format the response
    info_text = (
        "✨ **User Info** ✨\n\n"
        f"👤 **Full Name:** {full_name}\n"
        f"🔹 **Username:** {username}\n"
        f"🆔 **User ID:** `{user_id}`\n"
        f"🌍 **Profile Link:** {profile_link}\n"
        f"🗓 **Account Created:** {account_creation_date}\n"
        f"🚀 **Status:** {status}\n\n"
        f"📌 **Bio:** {bio}\n\n"
        "⚡ Powered by CyberNexus"
    )

    await event.edit(info_text)
