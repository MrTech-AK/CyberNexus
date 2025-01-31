from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

help_text = """
**CyberNexus Plugins List:**

1. `.admin` - Admin tools for managing users in your groups.
2. `.warn` - Warning system for handling user behavior.
3. `.tag` - Mass tagging for different user groups.
4. `.profile` - Manage your profile like name, bio, and picture.
5. `.pmpermit` - Control private messages with approval system.
6. `.schedule` - Schedule messages to be sent later.
7. `.globaltools` - Global admin tools for cross-group management.
8. `.greetings` - Manage welcome and goodbye messages for your groups.
9. `.chats` - Group and chat management tools.
10. `.calculator` - Open a simple calculator.
11. `.mute` - Mute/unmute users in your group or DMs.
12. `.font` - Generate text in Tʜɪs font.
13. `.notes` - Save, delete, and list your notes.

**Use `.help <plugin_name>` to get more details about any plugin.**
"""

plugin_help = {
    "admin": """**.admin plugin:**
    - `.admin promote <user>` - Promote a user to admin.
    - `.admin demote <user>` - Demote a user to normal user.
    - `.admin ban <user>` - Ban a user from the group.
    - `.admin unban <user>` - Unban a user.
    - `.admin kick <user>` - Kick a user from the group.
    - `.admin tban <time> <user>` - Temporarily ban a user.
    - `.admin pin <message>` - Pin a message.
    - `.admin unpin` - Unpin a message.
    - `.admin tpin <time> <message>` - Temporarily pin a message.
    - `.admin purge <count>` - Delete multiple messages.
    - `.admin purgeme <count>` - Delete your last `<count>` messages.
    - `.admin purgeall` - Delete all messages in the chat.
    - `.admin pinned` - Show the most recently pinned message.
    - `.admin listpinned` - List all pinned messages.
    - `.admin autodelete <time>` - Auto-delete messages after a set time.
    """,
    "warn": """**.warn plugin:**
    - `.warn <user>` - Warn a user.
    - `.resetwarn <user>` - Reset the warning count for a user.
    - `.warns <user>` - Show the number of warnings for a user.
    - `.setwarn <limit>` - Set the max warning limit before auto-action.
    """,
    "tag": """**.tag plugin:**
    - `.tag on` - Enable tagging of all users in the chat.
    - `.tag off` - Disable tagging.
    - `.tag all` - Tag all members.
    - `.tag bots` - Tag all bots in the chat.
    - `.tag rec` - Tag all recent members.
    - `.tag admins` - Tag all admins.
    - `.tag owner` - Tag the owner of the group.
    """,
    "profile": """**.profile plugin:**
    - `.setbio <bio>` - Set your bio.
    - `.setname <name>` - Set your name.
    - `.setpic <url>` - Set your profile picture.
    - `.delpfp` - Delete your profile picture.
    - `.poto` - Show your current profile picture.
    """,
    "pmpermit": """**.pmpermit plugin:**
    - `.block <user>` - Block a user from sending PMs.
    - `.unblock <user>` - Unblock a user.
    - `.listapproved` - Show the list of approved users.
    - `.a <user>` - Approve a user to send PMs.
    - `.d <user>` - Disapprove a user from sending PMs.
    **Note**: Users who send 10 messages without approval will be automatically blocked.
    """,
    "schedule": """**.schedule plugin:**
    - `.schedule <message> <time>` - Schedule a message to be sent later at the specified time.
    """,
    "globaltools": """**.globaltools plugin:**
    - `.gpromote <user>` - Promote a user globally.
    - `.gdemote <user>` - Demote a user globally.
    - `.ungban <user>` - Unban a user globally.
    - `.gban <user>` - Ban a user globally.
    - `.gcast <message>` - Send a message to all groups and admins.
    - `.gucast <message>` - Send a message to all private chats.
    - `.gkick <user>` - Kick a user from all groups.
    - `.gmute <user>` - Mute a user globally.
    - `.ungmute <user>` - Unmute a user globally.
    - `.listgban` - List globally banned users.
    - `.gstat` - Show global ban stats.
    - `.gblacklist <user>` - Blacklist a user globally.
    - `.ungblacklist <user>` - Remove a user from the global blacklist.
    """,
    "greetings": """**.greetings plugin:**
    - `.setwelcome <message>` - Set a welcome message.
    - `.clearwelcome` - Clear the welcome message.
    - `.getwelcome` - Get the current welcome message.
    - `.setgoodbye <message>` - Set a goodbye message.
    - `.cleargoodbye` - Clear the goodbye message.
    - `.getgoodbye` - Get the current goodbye message.
    - `.thankmembers <on|off>` - Enable/Disable thanking new members.
    """,
    "chats": """**.chats plugin:**
    - `.delchat` - Delete the entire chat history.
    - `.getlink` - Get the group invite link.
    - `.create (g|c)` - Create a group or channel.
    - `.setgpic` - Set the group profile picture.
    - `.delgpic` - Delete the group profile picture.
    - `.unbanall` - Unban all users.
    - `.rmusers` - Remove inactive users.
    """,
    "calculator": """**.calculator plugin:**
    - `.calc` - Open a calculator.
    """,
    "mute": """**.mute plugin:**
    - `.dmute <user>` - Mute a user in direct messages.
    - `.undmute <user>` - Unmute a user in direct messages.
    - `.tmute` - Temporarily mute a user.
    - `.unmute <user>` - Unmute a user.
    - `.mute <user>` - Mute a user.
    """,
    "fontgen": """**.font plugin:**
    - `.font <text>` - Generate text in Tʜɪs font.
    """,
    "notes": """**.notes plugin:**
    - `.addnote <note>` - Add a new note.
    - `.remnote <note_id>` - Remove a note by ID.
    - `.listnote` - List all saved notes.
    """
}

@client.on(events.NewMessage(pattern=r"^\.help$", outgoing=True))
async def help(event):
    """Send the general help text with a list of plugins."""
    await event.edit(help_text)

@client.on(events.NewMessage(pattern=r"^\.help (.*)$", outgoing=True))
async def plugin_help(event):
    """Send detailed help text for a specific plugin."""
    plugin = event.pattern_match.group(1).lower()
    if plugin in plugin_help:
        await event.edit(plugin_help[plugin])
    else:
        await event.edit("**Plugin not found!** Use `.help` to see the available plugins.")
