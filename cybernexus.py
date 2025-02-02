# cybernexus.py
import logging
from telethon import TelegramClient, events, Button, functions, types
from telethon.sessions import StringSession
from config import API_ID, API_HASH, STRING_SESSION, TELEGRAM_USERNAME, TELEGRAM_NAME, CMD_PREFIX, LOG_CHAT_ID

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CyberNexus")

# Initialize clients
user_client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
bot_client = None  # Will be initialized after creating the bot

# Welcome message for the bot
WELCOME_TEXT = f"""
Hello! I am {TELEGRAM_NAME}'s CyberNexus Assistant 🤖.

You can contact my owner directly using this bot. Use the buttons below to get started!
"""

ABOUT_NEXUS = """
**CyberNexus** is a powerful and versatile Telegram Userbot and Assistant Bot designed to simplify your experience.
Developed by a skilled creator, it provides features like message handling, cool inline menus, and much more!
"""

async def promote_bot_in_log_group():
    """Ensure the bot joins the log group and is promoted to admin."""
    try:
        # Add the bot to the log group
        result = await bot_client(functions.channels.InviteToChannelRequest(
            channel=int(LOG_CHAT_ID),
            users=[await bot_client.get_me()]
        ))
        logger.info("Bot successfully joined the log group.")
        
        # Promote the bot to admin
        await bot_client(functions.channels.EditAdminRequest(
            channel=int(LOG_CHAT_ID),
            user_id=await bot_client.get_me(),
            admin_rights=types.ChatAdminRights(
                change_info=False,
                post_messages=True,
                edit_messages=True,
                delete_messages=True,
                invite_users=True,
                restrict_users=True,
                pin_messages=True,
                add_admins=False,
                manage_call=True,
                anonymous=False
            ),
            rank="CyberNexus Bot"
        ))
        logger.info("Bot promoted to admin in the log group.")
        
        # Tag the owner in the log group
        await bot_client.send_message(
            int(LOG_CHAT_ID),
            f"✅ **CyberNexus Bot and Userbot have started successfully!**\n\n"
            f"Owner: [Here](https://t.me/{TELEGRAM_USERNAME})",
            parse_mode="md"
        )
    except Exception as e:
        logger.error(f"Error while promoting bot in log group: {e}")

async def start_userbot():
    """Function to start the userbot."""
    await user_client.start()
    logger.info("Userbot started successfully.")

    @user_client.on(events.NewMessage(pattern=f"{CMD_PREFIX}help"))
    async def help_command(event):
        """Help command for the userbot."""
        buttons = [[Button.inline("Command 1", data="cmd1"), Button.inline("Command 2", data="cmd2")]]
        await event.reply("**CyberNexus Userbot Help Menu**", buttons=buttons)

async def start_bot():
    """Function to start the bot."""
    global bot_client

    # Extract the bot token from BotFather setup
    with open("config.py") as config_file:
        lines = config_file.readlines()
        bot_token = None
        for line in lines:
            if "BOT_TOKEN" in line:
                bot_token = line.split("=")[1].strip().replace('"', '')
                break

    if not bot_token:
        logger.error("Bot token not found in config.py. Exiting...")
        return

    bot_client = TelegramClient("bot", API_ID, API_HASH).start(bot_token=bot_token)
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

async def main():
    """Main function to start userbot and bot."""
    await start_userbot()
    await start_bot()
    logger.info("CyberNexus Userbot and Bot are running...")

    # Keep both clients running
    await user_client.run_until_disconnected()
    await bot_client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
