from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

help_text = """
**🚀 Welcome to CyberNexus Plugins List! 🚀**

🔧 **Plugins You Can Use:**

1. **.admin** - Manage your group with admin tools! 👑
2. **.warn** - Keep track of warnings for users! ⚠️
3. **.tag** - Tag all your group members in a flash! 🏷️
4. **.profile** - Customize your profile like a pro! 📸
5. **.pmpermit** - Control PMs with approval system! 🔒
6. **.schedule** - Schedule messages and never forget! 📅
7. **.globaltools** - Manage across all groups! 🌍
8. **.greetings** - Customize welcome and goodbye messages! 🎉
9. **.chats** - Manage your group chats effortlessly! 💬
10. **.calculator** - Get quick calculations on the go! 🧮
11. **.mute** - Mute and unmute users in a click! 🤐
12. **.font** - Generate cool text with awesome fonts! 🖋️
13. **.notes** - Save and manage your important notes! 📝

👉 **To get more details about a plugin, type** `.help <plugin_name>`. For example: `.help admin` 😎
"""

plugin_help = {
    "admin": """**.admin plugin:**
    - `.admin promote <user>` - Promote a user to admin. 👑
    - `.admin demote <user>` - Demote a user to normal user. ⬇️
    - `.admin ban <user>` - Ban a user from the group. 🚫
    - `.admin unban <user>` - Unban a user. 🟢
    - `.admin kick <user>` - Kick a user from the group. 👢
    - `.admin tban <time> <user>` - Temporarily ban a user. ⏳
    - `.admin pin <message>` - Pin a message. 📌
    - `.admin unpin` - Unpin a message. 🔓
    - `.admin tpin <time> <message>` - Temporarily pin a message. ⏳📌
    - `.admin purge <count>` - Delete multiple messages. 🧹
    - `.admin purgeme <count>` - Delete your last `<count>` messages. 🧼
    - `.admin purgeall` - Delete all messages in the chat. 🗑️
    - `.admin pinned` - Show the most recently pinned message. 📌
    - `.admin listpinned` - List all pinned messages. 📋
    - `.admin autodelete <time>` - Auto-delete messages after a set time. ⏱️
    """,
    "warn": """**.warn plugin:**
    - `.warn <user>` - Warn a user. ⚠️
    - `.resetwarn <user>` - Reset the warning count for a user. 🔄
    - `.warns <user>` - Show the number of warnings for a user. 📊
    - `.setwarn <limit>` - Set the max warning limit before auto-action. 🚦
    """,
    "tag": """**.tag plugin:**
    - `.tag on` - Enable tagging of all users in the chat. 🎯
    - `.tag off` - Disable tagging. 🚫
    - `.tag all` - Tag all members. 👥
    - `.tag bots` - Tag all bots in the chat. 🤖
    - `.tag rec` - Tag all recent members. 👋
    - `.tag admins` - Tag all admins. 👑
    - `.tag owner` - Tag the owner of the group. 👑
    """,
    "profile": """**.profile plugin:**
    - `.setbio <bio>` - Set your bio. 📝
    - `.setname <name>` - Set your name. 💬
    - `.setpic <url>` - Set your profile picture. 📸
    - `.delpfp` - Delete your profile picture. ❌
    - `.poto` - Show your current profile picture. 🖼️
    """,
    "pmpermit": """**.pmpermit plugin:**
    - `.block <user>` - Block a user from sending PMs. 🚫
    - `.unblock <user>` - Unblock a user. 🔓
    - `.listapproved` - Show the list of approved users. ✅
    - `.a <user>` - Approve a user to send PMs. 🟢
    - `.d <user>` - Disapprove a user from sending PMs. 🔴
    **Note**: Users who send 10 messages without approval will be automatically blocked. ⚠️
    """,
    "schedule": """**.schedule plugin:**
    - `.schedule <message> <time>` - Schedule a message to be sent later at the specified time. 🗓️
    """,
    "globaltools": """**.globaltools plugin:**
    - `.gpromote <user>` - Promote a user globally. 🌍
    - `.gdemote <user>` - Demote a user globally. 🌍
    - `.ungban <user>` - Unban a user globally. 🟢
    - `.gban <user>` - Ban a user globally. 🚫
    - `.gcast <message>` - Send a message to all groups and admins. 📢
    - `.gucast <message>` - Send a message to all private chats. 📩
    - `.gkick <user>` - Kick a user from all groups. 👢
    - `.gmute <user>` - Mute a user globally. 🤐
    - `.ungmute <user>` - Unmute a user globally. 🔊
    - `.listgban` - List globally banned users. 📋
    - `.gstat` - Show global ban stats. 📊
    - `.gblacklist <user>` - Blacklist a user globally. 🚫
    - `.ungblacklist <user>` - Remove a user from the global blacklist. 🟢
    """,
    "greetings": """**.greetings plugin:**
    - `.setwelcome <message>` - Set a welcome message. 🎉
    - `.clearwelcome` - Clear the welcome message. 🧹
    - `.getwelcome` - Get the current welcome message. 💬
    - `.setgoodbye <message>` - Set a goodbye message. 👋
    - `.cleargoodbye` - Clear the goodbye message. 🧹
    - `.getgoodbye` - Get the current goodbye message. 💬
    - `.thankmembers <on|off>` - Enable/Disable thanking new members. 🙏
    """,
    "chats": """**.chats plugin:**
    - `.delchat` - Delete the entire chat history. 🗑️
    - `.getlink` - Get the group invite link. 🔗
    - `.create (g|c)` - Create a group or channel. 🆕
    - `.setgpic` - Set the group profile picture. 📸
    - `.delgpic` - Delete the group profile picture. ❌
    - `.unbanall` - Unban all users. 🟢
    - `.rmusers` - Remove inactive users. 🧹
    """,
    "calculator": """**.calculator plugin:**
    - `.calc` - Open a calculator. 🧮
    """,
    "mute": """**.mute plugin:**
    - `.dmute <user>` - Mute a user in direct messages. 🤐
    - `.undmute <user>` - Unmute a user in direct messages. 🔊
    - `.tmute` - Temporarily mute a user. ⏳🤐
    - `.unmute <user>` - Unmute a user. 🔊
    - `.mute <user>` - Mute a user. 🤐
    """,
    "fontgen": """**.font plugin:**
    - `.font <text>` - Generate text in Tʜɪs font. ✨
    """,
    "notes": """**.notes plugin:**
    - `.addnote <note>` - Add a new note. 📝
    - `.remnote <note_id>` - Remove a note by ID. ❌
    - `.listnote` - List all saved notes. 📋
    """
}

@client.on(events.NewMessage(pattern=r"^\.help(?:\s+(.+))?$", outgoing=True))
async def help_command(event):
    """Send general help or plugin-specific help."""
    match = event.pattern_match.group(1)  # Capture the plugin name if provided

    if not match:  # If no plugin is specified, send general help
        await event.edit(help_text)
        return

    plugin = match.lower().strip()  # Normalize the plugin name

    if plugin in plugin_help:
        await event.edit(plugin_help[plugin])
    else:
        await event.edit(f"**Plugin not found!**\nUse `.help` to see available plugins. 😕")
