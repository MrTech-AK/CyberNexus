from telethon import events
from cybernexus import client
import requests
import urllib.parse
import os
import platform 

@client.on(events.NewMessage(pattern=r"^\.carbon (.+)$", outgoing=True))
async def carbon(event):
    """CyberNexus Carbon Code Snippet Generator"""
    
    code = event.pattern_match.group(1)
    await event.edit("🎨 **Generating Code Snippet...**\n\n⚡ Powered by CyberNexus")

    # Encode the code for URL usage
    encoded_code = urllib.parse.quote(code)

    # Carbon API URL (generates the snippet)
    url = f"https://carbon.now.sh/?bg=rgba(0,0,0,0)&t=blackboard&wt=none&l=python&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira+Code&code={encoded_code}"

    # Save image
    img_path = "carbon.png"
    response = requests.get(f"https://thumbnails.carbon.now.sh/{encoded_code}")
    if response.status_code == 200:
        with open(img_path, "wb") as img_file:
            img_file.write(response.content)

        # Send the image
        await event.delete()
        await client.send_file(event.chat_id, img_path, caption="🖼️ **Carbon Code Snippet**\n\n⚡ Powered by CyberNexus")
        os.remove(img_path)
    else:
        await event.edit("❌ **Error: Unable to generate Carbon snippet!**")
