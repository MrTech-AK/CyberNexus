from telethon import events
from cybernexus import client
import calendar
import platform 

@client.on(events.NewMessage(pattern=r"^\.calendar (\d+) (\d+)$", outgoing=True))
async def show_calendar(event):
    """CyberNexus Monthly Calendar Generator"""
    
    try:
        month, year = int(event.pattern_match.group(1)), int(event.pattern_match.group(2))
        cal = calendar.month(year, month)
        await event.edit(f"📅 **Calendar for {month}/{year}**\n```{cal}```")
    
    except Exception:
        await event.edit("❌ **Invalid Input!**\nUsage: `.calendar <month> <year>`")
