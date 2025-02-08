from telethon import events
from cybernexus import client
import requests
import os
import platform 

@client.on(events.NewMessage(pattern=r"^\.download (.+)$", outgoing=True))
async def download_file(event):
    """CyberNexus File Downloader Plugin"""
    
    url = event.pattern_match.group(1)
    file_name = url.split("/")[-1]
    
    await event.edit(f"📥 **Downloading `{file_name}`...**")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        
        await client.send_file(event.chat_id, file_name, caption=f"📁 **Downloaded File:** `{file_name}`")
        os.remove(file_name)
    else:
        await event.edit("❌ **Error: Unable to download file!**")
