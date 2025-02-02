from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Schedule message list to store the scheduled messages and their times
scheduled_messages = []

@client.on(events.NewMessage(pattern=r"^\.schedule (.+) (\d+)$", outgoing=True))
async def schedule_message(event):
    """Handles the scheduling of messages."""
    # Extract the message and time (in seconds)
    message = event.pattern_match.group(1)
    time_delay = int(event.pattern_match.group(2))
    
    # Store the scheduled message
    scheduled_messages.append({
        "message": message,
        "time_delay": time_delay
    })

    # Acknowledge that the message has been scheduled
    await event.edit(f"**Scheduled message:**\n"
                     f"Message: {message}\n"
                     f"Time: {time_delay} seconds from now.\n\n"
                     "I will send it once the time is up!")

    # Wait for the specified time and then send the message
    time.sleep(time_delay)
    await client.send_message(event.chat_id, message)
    scheduled_messages.remove({"message": message, "time_delay": time_delay})


@client.on(events.NewMessage(pattern=r"^\.help_schedulemsg$", outgoing=True))
async def schedule_help(event):
    """Displays help for the .schedule command."""
    help_message = (
        "✵ **ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ .sᴄʜᴇᴅᴜʟᴇ** ✵\n\n"
        "• `.schedule <msg> <time>` – ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ sᴄʜᴇᴅᴜʟᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛʜᴀᴛ ᴡɪʟʟ ʙᴇ sᴇɴᴛ ᴀɢᴀɪɴsᴛ ᴛʜᴇ ɢɪvᴇɴ ᴛɪᴍᴇ.\n"
        "    ᴀᴇ.g. `.schedule Hello 60` ᴡɪʟʟ sᴇɴᴅ `Hello` ᴀғᴛᴇʀ 60 sᴇᴄᴏɴᴅs.\n\n"
        "ᴅᴏ ɴᴏᴛ ɪɴᴄʟᴜᴅᴇ sᴘᴀᴄᴇs ɪɴ ʏᴏᴜʀ ᴛɪᴍᴇ ᴇxᴄᴇᴘᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ!"
    )
    await event.edit(help_message)
