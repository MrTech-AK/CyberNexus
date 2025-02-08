import platform
import psutil
import time
from telethon import events
from cybernexus import client

start_time = time.time()  # Track bot uptime

@client.on(events.NewMessage(pattern=r"^\.sysinfo$", outgoing=True))
async def sysinfo(event):
    """Fetches system information."""
    uname = platform.uname()
    os_info = f"{uname.system} {uname.release} ({uname.version})"
    cpu = f"{psutil.cpu_count(logical=True)} Cores"
    ram = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    disk = f"{round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB"
    python_version = platform.python_version()
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))

    info = f"""
    🖥 **System Info** 🖥

    🔹 **OS:** {os_info}
    🔹 **CPU:** {cpu}
    🔹 **RAM:** {ram}
    🔹 **Disk Space:** {disk}
    🔹 **Python:** {python_version}
    🔹 **Uptime:** {uptime}

    ⚡ Powered By CyberNexus
    """

    await event.edit(info)
