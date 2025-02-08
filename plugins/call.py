import time
from telethon import events
from cybernexus import client

@client.on(events.NewMessage(pattern=r"^\.call$", outgoing=True))
def fake_call(event):
    """Fake Call Animation with Telegram HQ via CyberNexus"""
    
    call_steps = [
        "📡 **Dialing Telegram Secure Line...**",
        "📞 **Initiating Encrypted Connection...**",
        "🔍 **Authenticating User...**",
        "🔐 **User Verified! Accessing Telegram Secure Server...**",
        "📲 **Connecting to Telegram Headquarters...**",
        "📞 **Call Connected.**",
        "🎤 **Telegram AI:** Hello, this is Telegram Headquarters. Please state your identity.",
        "🗣 **Me:** Yo, this is `CyberNexus AI`! Connect me to Pavel Durov immediately!",
        "✅ **Request Approved. Establishing Direct Contact...**",
        "📞 **Calling Pavel Durov...**",
        "📍 **Tracing Location...**",
        "📡 **Securing Line...**",
        "🔗 **Connection Established.**",
        "🎤 **Pavel:** Who is this? How did you get this number?!",
        "🗣 **Me:** Relax, bro! It's me, the creator of CyberNexus! 😎",
        "😲 **Pavel:** WHAT!? CyberNexus?! No way! You’re a legend!",
        "🔥 **Pavel:** Bro, I need your help ASAP!",
        "🛠 **Pavel:** Telegram v70.0 has a critical bug. Messages aren’t deleting properly!",
        "💻 **Me:** Send me the source code. I’ll fix it right now!",
        "📨 **Pavel:** Sending `telegram_secret_dev.zip`...",
        "📂 **File Received. Extracting Source Code...**",
        "🔍 **Scanning for Vulnerabilities...**",
        "⚠ **Critical Bug Detected in Core API!**",
        "🔧 **Fixing Telegram’s Security Loopholes...**",
        "🚀 **Optimizing Cloud Servers...**",
        "💾 **Saving & Deploying Fix...**",
        "📤 **Uploading Telegram v70.1 Patch...**",
        "🔄 **Global Update Rolling Out...**",
        "✅ **Telegram Update Complete! Security Improved!**",
        "🎉 **Pavel:** OMG! You did it! CyberNexus is the best!",
        "👑 **Me:** Haha, anytime bro! Telegram is now 10x better!",
        "🤝 **Pavel:** Thanks, legend! Let’s collab on Telegram AI next time!",
        "📴 **Private Call Disconnected.**",
    ]

    for step in call_steps:
        event.edit(step)
        time.sleep(2)  # No asyncio, just time.sleep()
