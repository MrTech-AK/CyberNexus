from telethon import events
from cybernexus import client
import aiohttp
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import

GITHUB_API = "https://api.github.com/users/"

@client.on(events.NewMessage(pattern=r"^\.github (\S+)$"))
async def github_info(event):
    username = event.pattern_match.group(1)
    url = f"{GITHUB_API}{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return await event.reply("❌ User not found!")
            
            data = await response.json()

    message = (
        f"✨ **GitHub Info** ✨\n\n"
        f"👤 **Name:** {data.get('name', 'N/A')}\n"
        f"🔹 **Username:** {data['login']}\n"
        f"🆔 **User ID:** {data['id']}\n"
        f"📌 **Public Repos:** {data['public_repos']}\n"
        f"🌟 **Followers:** {data['followers']} | **Following:** {data['following']}\n"
        f"🔗 **Profile:** [Click Here]({data['html_url']})\n"
        f"📅 **Account Created:** {data['created_at'][:10]}\n\n"
        f"⚡ **Powered By CyberNexus**"
    )

    await event.reply(message)
