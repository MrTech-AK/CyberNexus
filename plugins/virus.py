from telethon import events
from cybernexus import client
import asyncio  # Use asyncio for async delays
import platform 

@client.on(events.NewMessage(pattern=r"^\.virus$", outgoing=True))
async def virus_upload(event):
    """CyberNexus Virus Uploading & Phone Crash Animation"""

    virus_steps = [
        "☠ **Initializing CyberNexus Virus...**",
        "💾 **Loading Malicious Code...**",
        "🔍 **Scanning Target Device...**",
        "📡 **Connecting to Remote Server...**",
        "🛠 **Injecting Trojan Script...**",
        "📂 **Extracting Personal Data...**",
        "🔓 **Disabling Security Protocols...**",
        "📤 **Uploading CyberNexus Payload...**",
        "⚠ **Device Warning: Unauthorized Activity Detected!**",
        "📡 **Establishing Backdoor Connection...**",
        "🔄 **Deploying Ransomware Encryption...**",
        "🚀 **Overclocking CPU to 500%...**",
        "🔥 **Overheating Detected! Device Shutdown Imminent!**",
        "💀 **Erasing System Files...**",
        "📵 **Critical Error: Device Bricked!**",
        "🔁 **Rebooting in 3... 2... 1...**",
        "💣 **💥 BOOM!! System Destroyed! 💀**",
        "✅ **Mission Complete! CyberNexus Rules!**"
    ]

    for step in virus_steps:
        await event.edit(step)  # Use await to prevent sync issues
        await asyncio.sleep(2)  # Use asyncio.sleep() instead of time.sleep()
