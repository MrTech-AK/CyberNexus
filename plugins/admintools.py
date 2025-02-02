from telethon import events
from telethon.tl.custom import InlineKeyboardButton, InlineKeyboardMarkup
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Function to handle the ".admin" command and show the tools menu
@client.on(events.NewMessage(pattern=r".admin", outgoing=True))
async def admin_tools(event):
    if event.is_private:
        return  # Avoid private messages for admin tools
    
    user = await event.get_sender()
    username = user.username if user.username else "Unknown"
    
    # Display a message with the options for admin tools
    if event.text.startswith(".admin help"):
        help_text = """
        🔹 **CyberNexus Admin Tools** 🔹\n\n
        **User Management:**\n
        ➤ `.admin promote` – Promote a user to admin.\n
        ➤ `.admin demote` – Demote an admin to a normal user.\n
        ➤ `.admin ban` – Ban a user from the group.\n
        ➤ `.admin unban` – Unban a user.\n
        ➤ `.admin kick` – Kick a user from the group.\n
        ➤ `.admin tban <time>` – Temporarily ban a user.\n\n
        **Message Management:**\n
        ➤ `.admin pin` – Pin a message.\n
        ➤ `.admin unpin` – Unpin the last pinned message.\n
        ➤ `.admin tpin <time>` – Temporarily pin a message.\n
        ➤ `.admin purge` – Delete multiple messages in bulk.\n
        ➤ `.admin purgeme <count>` – Delete your last `<count>` messages.\n
        ➤ `.admin purgeall` – Delete **all** messages in the chat.\n\n
        **Pinned Messages:**\n
        ➤ `.admin pinned` – Show the most recently pinned message.\n
        ➤ `.admin listpinned` – List all pinned messages in the chat.\n\n
        **Auto Management:**\n
        ➤ `.admin autodelete <time>` – Auto-delete messages after a set time.\n
        """
        await event.reply(help_text)

        # Create the inline keyboard with cool buttons
        buttons = [
            [InlineKeyboardButton("💼 User Management", callback_data="user_management")],
            [InlineKeyboardButton("📑 Message Management", callback_data="message_management")],
            [InlineKeyboardButton("📌 Pinned Messages", callback_data="pinned_messages")],
            [InlineKeyboardButton("⚙️ Auto Management", callback_data="auto_management")]
        ]
        
        # Making the layout cooler with some style
        reply_markup = InlineKeyboardMarkup(buttons)
        await event.reply("Welcome to **CyberNexus Admin Tools**! Choose a category below:", reply_markup=reply_markup)

# Function to handle button presses and show the respective commands
@client.on(events.CallbackQuery)
async def callback_query_handler(event):
    if event.data == b"user_management":
        await event.answer("⚡ **User Management Commands** ⚡\n"
                           "➤ `.admin promote` – Promote a user to admin.\n"
                           "➤ `.admin demote` – Demote an admin to a normal user.\n"
                           "➤ `.admin ban` – Ban a user from the group.\n"
                           "➤ `.admin unban` – Unban a user.\n"
                           "➤ `.admin kick` – Kick a user from the group.\n"
                           "➤ `.admin tban <time>` – Temporarily ban a user.", alert=True)
    
    elif event.data == b"message_management":
        await event.answer("📝 **Message Management Commands** 📝\n"
                           "➤ `.admin pin` – Pin a message.\n"
                           "➤ `.admin unpin` – Unpin the last pinned message.\n"
                           "➤ `.admin tpin <time>` – Temporarily pin a message.\n"
                           "➤ `.admin purge` – Delete multiple messages in bulk.\n"
                           "➤ `.admin purgeme <count>` – Delete your last `<count>` messages.\n"
                           "➤ `.admin purgeall` – Delete **all** messages in the chat.", alert=True)
    
    elif event.data == b"pinned_messages":
        await event.answer("📌 **Pinned Messages Commands** 📌\n"
                           "➤ `.admin pinned` – Show the most recently pinned message.\n"
                           "➤ `.admin listpinned` – List all pinned messages in the chat.", alert=True)
    
    elif event.data == b"auto_management":
        await event.answer("⚙️ **Auto Management Commands** ⚙️\n"
                           "➤ `.admin autodelete <time>` – Auto-delete messages after a set time.", alert=True)

# Run the client
client.run_until_disconnected()
