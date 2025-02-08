from telethon import events
from cybernexus import client
import os
import platform 

@client.on(events.NewMessage(pattern=r"^\.tts (.+)$", outgoing=True))
async def text_to_speech(event):
    """CyberNexus Text-to-Speech Plugin"""
    
    text = event.pattern_match.group(1)
    file_path = "speech.mp3"
    
    os.system(f"espeak -v en '{text}' -w {file_path}")  # Uses eSpeak TTS engine
    
    await client.send_file(event.chat_id, file_path, caption="🔊 **Text-to-Speech Output**")
    os.remove(file_path)
