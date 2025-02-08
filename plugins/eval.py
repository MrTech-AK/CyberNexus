from telethon import events
from cybernexus import client
import io
import sys
import platform

@client.on(events.NewMessage(pattern=r"^\.eval\s+(.+)", outgoing=True))
async def evaluate(event):
    """Evaluates Python code securely in an isolated environment."""
    code = event.pattern_match.group(1).strip()
    
    safe_env = {}  # Secure environment
    
    # Capture stdout (for print statements)
    output_buffer = io.StringIO()
    sys.stdout = output_buffer
    
    try:
        exec(code, safe_env)  # Execute code safely
        output = output_buffer.getvalue().strip()  # Get printed output
        if not output:
            output = "✅ **Executed Successfully!** (No Output)"
    except Exception as e:
        output = f"❌ **Error:** `{str(e)}`"
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    await event.edit(f"🔍 **Evaluated:**\n```{code}```\n\n📝 **Output:**\n```{output}```")
