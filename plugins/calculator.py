from telethon import events
from cybernexus import client
import config
import time
import sys
import math
import ast
import telethon
import platform


# Dictionary to track users in calculator mode
calculator_mode = {}

@client.on(events.NewMessage(pattern=r"^\.calc$", outgoing=True))
async def calc(event):
    """Activates calculator mode for the user."""
    user_id = event.sender_id
    calculator_mode[user_id] = True  # Mark user as active in calculator mode

    await event.edit(
        "**🔢 CyberNexus Calculator Activated!**\n\n"
        "I can perform basic math operations like:\n"
        "`2 + 2`, `3 * 5`, `10 / 2`, `sqrt(16)`, `pow(2, 3)`, `sin(math.radians(90))`\n\n"
        "**Send a math expression, and I'll calculate it for you.**\n"
        "To exit, type `.exit_calc` 🚪."
    )

@client.on(events.NewMessage(outgoing=True))
async def calculate_expression(event):
    """Evaluates user input if they are in calculator mode."""
    user_id = event.sender_id
    message = event.raw_text.strip()

    # Check if user is in calculator mode
    if user_id not in calculator_mode:
        return

    # Handle exit command
    if message.lower() == ".exit_calc":
        del calculator_mode[user_id]  # Remove user from calculator mode
        return await event.respond("**👋 Exiting calculator mode.** Type `.calc` to start again.")

    # Prevent processing bot commands inside calculator mode
    if message.startswith("."):
        return

    try:
        # Evaluate the mathematical expression safely
        result = eval_expression(message)
        await event.respond(f"**✅ Result:** `{result}`")
    except ValueError as e:
        await event.respond(f"**❌ Error:** `{str(e)}`. Try again!")

def eval_expression(expression):
    """Safely evaluates a mathematical expression using AST parsing."""
    allowed_functions = {
        "math": math,
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "pow": pow,
        "abs": abs,
        "round": round,
        "radians": math.radians
    }

    try:
        node = ast.parse(expression, mode="eval")  # Parse expression safely

        # Ensure only safe operations are used
        for subnode in ast.walk(node):
            if isinstance(subnode, ast.Name) and subnode.id not in allowed_functions:
                raise ValueError(f"Unsupported function: `{subnode.id}`")
            elif not isinstance(subnode, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Load, ast.Call, ast.Attribute)):
                raise ValueError("Unsupported operation detected!")

        return eval(compile(node, "<string>", "eval"), {"__builtins__": {}}, allowed_functions)

    except Exception:
        raise ValueError("Invalid expression. Please use only supported mathematical operations.")

@client.on(events.NewMessage(pattern=r"^\.help_calc$", outgoing=True))
async def help_calc(event):
    """Provides help for the calculator feature."""
    await event.edit(
        "**🧮 CyberNexus Calculator Help**\n\n"
        "Usage:\n"
        "1. Type `.calc` to enter calculator mode.\n"
        "2. Send a math expression, and I'll calculate it for you.\n"
        "   Examples:\n"
        "   - `2 + 2` → `4`\n"
        "   - `3 * 5` → `15`\n"
        "   - `10 / 2` → `5.0`\n"
        "3. Advanced functions:\n"
        "   - `sqrt(16)` → `4.0`\n"
        "   - `pow(2, 3)` → `8`\n"
        "   - `sin(math.radians(90))` → `1.0`\n"
        "4. Exit with `.exit_calc` anytime 🚪.\n"
        "5. Restart calculator mode with `.calc` 🔄."
    )
