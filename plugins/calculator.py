from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.calc$", outgoing=True))
async def calc(event):
    """Opens a simple calculator and handles basic mathematical expressions."""
    await event.edit(
        "**🔢 Welcome to the CyberNexus Calculator!**\n"
        "I can help you with basic mathematical operations like:\n\n"
        "`2 + 2`, `3 * 5`, `10 / 2`, `sqrt(16)`\n\n"
        "**Type any expression below and I'll calculate it for you.**\n"
        "To exit the calculator anytime, just type `.exit_calc` 🚪."
    )

    @client.on(events.NewMessage(outgoing=True, func=lambda e: e.is_private))
    async def calculate_expression(event):
        """Evaluates the mathematical expression."""
        try:
            # Get the user input (expression)
            expression = event.raw_text
            
            # Check if the user typed an expression after .calc command or just hit enter
            if expression.startswith(".calc") or expression == '':
                return
            
            # Handle exit command
            if expression.lower() == ".exit_calc":
                return await event.respond("**👋 Exiting calculator mode.** Type `.calc` to start again.")

            # Try to evaluate the expression
            result = eval(expression)
            await event.respond(f"**✅ Result:** {result}")
        
        except Exception as e:
            await event.respond(f"**❌ Error:** Invalid expression or syntax. Please try again!")


@client.on(events.NewMessage(pattern=r"^\.help_calc$", outgoing=True))
async def help_calc(event):
    """Provides help for the calculator feature."""
    await event.edit(
        "**🧮 CyberNexus Calculator Help**\n\n"
        "Here’s how you can use the calculator:\n"
        "1. Type any mathematical expression, and I'll calculate it for you.\n"
        "    Examples:\n"
        "    `2 + 2` → 4\n"
        "    `3 * 5` → 15\n"
        "    `10 / 2` → 5.0\n"
        "2. You can also use advanced functions like:\n"
        "    `sqrt(16)` → 4.0\n"
        "    `2 ** 3` → 8 (Exponentiation)\n\n"
        "3. To exit, type `.exit_calc` anytime 🚪.\n"
        "4. You can always type `.calc` to start the calculator mode again 🔄."
    )
