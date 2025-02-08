import os
import re
import yt_dlp
import aiohttp
from telethon import events
from cybernexus import client
import platform 

@client.on(events.NewMessage(pattern=r"^\.song (.+)", outgoing=True))
async def song_download(event):
    """Downloads a song from YouTube and sends it."""
    query = event.pattern_match.group(1)
    await event.edit(f"🎵 **Searching for:** `{query}`...")

    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as resp:
            html = await resp.text()
            video_ids = re.findall(r"watch\?v=(.{11})", html)
            if not video_ids:
                return await event.edit("❌ **No results found!**")

    video_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
    
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": "%(title)s.%(ext)s",
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            file_name = f"{info['title']}.mp3"

        await event.client.send_file(event.chat_id, file_name, caption=f"🎵 **Song:** `{info['title']}`\n⚡ Powered by CyberNexus")
        os.remove(file_name)
        await event.delete()
    except Exception as e:
        await event.edit(f"❌ **Error:** {str(e)}")
