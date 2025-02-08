import os
import time
import subprocess
from telethon import events
from cybernexus import client
import platform 

@client.on(events.NewMessage(pattern=r"^\.ytdl (.+)", outgoing=True))
async def youtube_download(event):
    """Download YouTube Video/Audio."""
    url = event.pattern_match.group(1)
    
    await event.edit("🎬 **Fetching video details...**")
    time.sleep(1)
    
    # Get video info
    cmd_info = f'yt-dlp -F "{url}"'
    process = subprocess.Popen(cmd_info, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        await event.edit(f"❌ **Error fetching video details:**\n`{error.decode()}`")
        return
    
    await event.edit("⏳ **Downloading... Please wait...**")
    
    # Download best quality video
    cmd_download = f'yt-dlp -f best "{url}" -o "downloaded_video.%(ext)s"'
    process = subprocess.Popen(cmd_download, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate()
    
    if not os.path.exists("downloaded_video.mp4"):
        await event.edit("❌ **Download failed!**")
        return
    
    await event.edit("✅ **Download complete! Uploading...**")
    
    # Upload the video
    await client.send_file(event.chat_id, "downloaded_video.mp4", caption="🎥 **Here is your video!**\n⚡ Powered by CyberNexus")
    os.remove("downloaded_video.mp4")
