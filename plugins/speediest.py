from telethon import events
from cybernexus import client
import speedtest
import platform 

@client.on(events.NewMessage(pattern=r"^\.speedtest$", outgoing=True))
async def speed_test(event):
    """CyberNexus Internet Speed Test"""
    
    await event.edit("⏳ **Running Speed Test...**")
    
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    result = f"""
    📶 **Internet Speed Test Results**
    🔻 **Download:** {download:.2f} Mbps
    🔺 **Upload:** {upload:.2f} Mbps
    🏓 **Ping:** {ping:.2f} ms
    """
    
    await event.edit(result)
