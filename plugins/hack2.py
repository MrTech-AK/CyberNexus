from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import
import asyncio

@client.on(events.NewMessage(pattern=r"^\.hack2$", outgoing=True))
async def fake_hack(event):
    """CyberNexus Fake Hacking Animation (Async Version)"""
    
    hack_steps = [
        "💻 **Initializing CyberNexus Hack Engine...**",
        "🔍 **Searching for Target IP...**",
        "📡 **Connecting to Secure Network...**",
        "🔓 **Bypassing Firewall...**",
        "🔑 **Cracking Encryption Keys...**",
        "📂 **Accessing Secure Database...**",
        "📡 **Hacking Into Telegram Secure Server...**",
        "🕵 **Extracting Sensitive Data...**",
        "📤 **Uploading CyberNexus Rootkit...**",
        "🛠 **Compromising System Security...**",
        "🚀 **Gaining Admin Privileges...**",
        "✅ **Access Granted! Root Permissions Enabled.**",
        "📨 **Downloading Encrypted Files...**",
        "🔍 **Decrypting Files...**",
        "📂 **Extracting Sensitive Information...**",
        "📤 **Uploading Payload...**",
        "💣 **Deploying CyberNexus Exploit...**",
        "🚀 **Server Breach Successful! Full Control Acquired!**",
        "📨 **Sending Stolen Data to Secure Cloud...**",
        "🔄 **Covering Tracks & Clearing Logs...**",
        "✅ **Hack Complete! Target System Compromised!**",
        "😎 **CyberNexus Has Taken Over the System!**",
        "👑 **Mission Complete. Cyber Attack Successful.**"
    ]

    for step in hack_steps:
        await event.edit(step)
        await asyncio.sleep(2)  # Async sleep
