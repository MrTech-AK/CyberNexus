import os
from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import



@client.on(events.NewMessage(pattern=r"^\.rename (\S+)$"))
async def rename_file(event):
    if not event.reply_to_msg_id:
        return await event.reply("❌ Reply to a file to rename it!")

    reply = await event.get_reply_message()
    if not reply.media:
        return await event.reply("❌ Reply must be to a file!")

    new_name = event.pattern_match.group(1)
    file_path = await client.download_media(reply, "downloads/")
    
    new_path = f"downloads/{new_name}"
    os.rename(file_path, new_path)

    await event.reply(f"✅ File renamed to **{new_name}**", file=new_path)
    os.remove(new_path)  # Clean up after sending
