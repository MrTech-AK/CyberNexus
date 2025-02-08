from telethon import events
from cybernexus import client
import sys
import io
import traceback
import platform 

@client.on(events.NewMessage(pattern=r"^\.eval (.+)", outgoing=True))
async def evaluate(event):
    """Evaluates Python expressions securely."""
    code = event.pattern_match.group(1)

    # Restrict dangerous built-in functions
    allowed_builtins = {
        "abs": abs, "round": round, "len": len, "min": min, "max": max, "sum": sum,
        "sorted": sorted, "filter": filter, "map": map, "zip": zip, "enumerate": enumerate
    }

    # Redirect stdout to capture output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        # Create a safe environment for evaluation
        safe_env = {"__builtins__": allowed_builtins}
        exec(f"result = {code}", safe_env)
        output = safe_env.get("result", "No output")
    except Exception as e:
        output = traceback.format_exc()

    # Restore stdout
    sys.stdout = old_stdout

    # Send result
    await event.edit(f"**🔍 Evaluated:**\n`{code}`\n\n**📝 Output:**\n`{output}`")
