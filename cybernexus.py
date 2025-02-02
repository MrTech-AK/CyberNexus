import os
import asyncio
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerUser
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from telethon import Button
import config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CyberNexus")

# Replace these values with the actual values from config.py
API_ID = config.API_ID
API_HASH = config.API_HASH
BOT_TOKEN = config.BOT_TOKEN  # The Bot Token from BotFather
TELEGRAM_USERNAME = config.TELEGRAM_USERNAME
LOG_CHAT_ID = config.LOG_CHAT_ID  # The log group/chat ID

# Welcome text when the bot starts
WELCOME_TEXT = "Hello! I am CyberNexus, your assistant bot. How can I help you today?"
ABOUT_NEXUS = "CyberNexus is a powerful userbot built to manage your messages and help you with your tasks."

async def promote_bot_in_log_group():
    """Promote the bot in the log group to admin with all required permissions."""
    logger.info("Promoting bot to admin in the log group...")
    log_group = await bot_client.get_entity(LOG_CHAT_ID)
    try:
        # Promote bot to admin with all permissions
        await bot_client.edit_admin(log_group, bot_client.get_me(), is_admin=True, 
                                     change_info=True, post_messages=True, delete_messages=True,
                                     invite_to_channel=True, ban_users=True)
        logger.info("Bot promoted to admin in log group.")
    except Exception as e:
        logger.error(f"Failed to promote bot: {e}")

async def start_bot():
    """Function to start the bot."""
    global bot_client

    # Initialize the bot client
    bot_client = TelegramClient("bot", API_ID, API_HASH)

    # Start the bot client with bot token
    await bot_client.start(bot_token=BOT_TOKEN)

    logger.info("Bot started successfully.")

    @bot_client.on(events.NewMessage(func=lambda e: e.is_private))
    async def contact_handler(event):
        """Handle incoming messages to the bot."""
        user = await event.get_sender()
        await event.reply(
            f"Hello, {user.first_name}! Your message has been forwarded to my owner.",
            buttons=[[Button.url("Contact Owner", f"https://t.me/{TELEGRAM_USERNAME}")]]
        )
        # Forward the message to the log group
        await bot_client.send_message(
            int(LOG_CHAT_ID),
            f"**New Message from {user.first_name}**\n\n{event.text}"
        )

    @bot_client.on(events.NewMessage(pattern="/start"))
    async def start_message(event):
        """Send the startup message with inline buttons."""
        buttons = [
            [Button.inline("About Nexus", data="about_nexus"), Button.url("Contact Owner", f"https://t.me/{TELEGRAM_USERNAME}")],
            [Button.inline("Help", data="help_menu")]
        ]
        await event.reply(WELCOME_TEXT, buttons=buttons)

    @bot_client.on(events.CallbackQuery(data="about_nexus"))
    async def about_nexus(event):
        """Handle the About Nexus button."""
        await event.edit(ABOUT_NEXUS)

    @bot_client.on(events.CallbackQuery(data="help_menu"))
    async def help_menu(event):
        """Handle the Help button."""
        await event.edit("**Help Menu**\n\nUse this bot to send messages to my owner!")

    # Promote bot in the log group
    await promote_bot_in_log_group()

# Main function to start the bot and userbot
async def main():
    """Start the userbot and bot simultaneously."""
    logger.info("Userbot started successfully.")
    await start_bot()

if __name__ == "__main__":
    try:
        # Start the event loop
        asyncio.run(main())
    except Exception as e:
        logger.error(f"An error occurred: {e}")
