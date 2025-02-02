from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

# Available font styles
font_styles = {
    "Tʜɪs": lambda text: ''.join([chr(ord(c) - 32 + 0x1D00) for c in text]),  # Tʜɪs font
    "c̑̈y̑̈b̑̈ȇ̈ȓ̈n̑̈ȇ̈x̑̈ȗ̈s̑̈": lambda text: ''.join([f"{c}\u0302\u0308" for c in text]),  # c̑̈y̑̈b̑̈ȇ̈ȓ̈n̑̈ȇ̈x̑̈ȗ̈s̑̈ font
    "c̆̈y̆̈b̆̈ĕ̈r̆̈n̆̈ĕ̈x̆̈ŭ̈s̆̈": lambda text: ''.join([f"{c}\u0314\u0308" for c in text]),  # c̆̈y̆̈b̆̈ĕ̈r̆̈n̆̈ĕ̈x̆̈ŭ̈s̆̈ font
    "༙c༙y༙b༙e༙r༙n༙e༙x༙u༙s༙": lambda text: ''.join([f"{c}\u0f99" for c in text]),  # ༙ font
    "🄲🅈🄱🄴🅁🄽🄴🅇🅄🅂": lambda text: ''.join([f"\U0001F170\U0001F194" for c in text]),  # 🄲🅈🄱🄴🅁🄽🄴🅇🅄🅂 font
    "𝖼𝓎𝒷𝑒𝓇𝓃𝑒𝓍𝓊𝓈": lambda text: ''.join([f"{c}\u1D52" for c in text]),  # 𝖼𝓎𝒷𝑒𝓇𝓃𝑒𝓍𝓊𝓈 font
    "𝓬𝔂𝓫𝓮𝓻𝓷𝓮𝓍𝓾𝓼": lambda text: ''.join([f"{c}\u1D4F" for c in text]),  # 𝓬𝔂𝓫𝓮𝓻𝓷𝓮𝓍𝓾𝓼 font
    "𝒸𝓎𝒷𝑒𝓇𝓃𝑒𝓍𝓊𝓈": lambda text: ''.join([f"{c}\u1D2C" for c in text]),  # 𝒸𝓎𝒷𝑒𝓇𝓃𝑒𝓍𝓊𝓈 font
}

# Command for generating text in specific fonts based on number
@client.on(events.NewMessage(pattern=r"^\.font (.+) (\d+)$", outgoing=True))
async def fontgen(event):
    """Generate text in a specific font based on the number."""
    text = event.pattern_match.group(1)  # Get the text after .font
    font_number = int(event.pattern_match.group(2))  # Get the font number

    # Check if the font number is valid
    if font_number < 1 or font_number > len(font_styles):
        return await event.edit("**❗ Invalid font option. Please choose a valid number.**")

    # Get the font style
    font_name = list(font_styles.keys())[font_number - 1]
    font_text = font_styles[font_name](text)

    await event.edit(f"**Generated text in {font_name} font:**\n{font_text}")

# Command for showing all fonts if no number is provided
@client.on(events.NewMessage(pattern=r"^\.font (.+)$", outgoing=True))
async def fontgen_all(event):
    """Generate text in all available fonts if no number is provided."""
    text = event.pattern_match.group(1)  # Get the text after .font

    if not text:
        return await event.edit("**❗ Please provide text to transform into a font.**")

    await event.edit(f"**💫 Available Fonts:**\n"
                     "`Tʜɪs`, `c̑̈y̑̈b̑̈ȇ̈ȓ̈n̑̈ȇ̈x̑̈ȗ̈s̑̈`, `c̆̈y̆̈b̆̈ĕ̈r̆̈n̆̈ĕ̈x̆̈ŭ̈s̆̈`, `༙c༙y༙b༙e༙r༙n༙e༙x༙u༙s༙`, and more...\n"
                     "**📝 Type your text and I'll show it in various fonts!**\n"
                     f"**Example:** `.font cybernexus`")

    # Iterate over fonts and generate text
    for name, font in font_styles.items():
        await event.respond(f"**{name}:**\n{font(text)}")

# Help command for fontgen
@client.on(events.NewMessage(pattern=r"^\.help_fontgen$", outgoing=True))
async def help_fontgen(event):
    """Provides help for the font generation feature."""
    await event.edit(
        "**🧑‍🏫 Font Generator Help**\n\n"
        "Here's how you can use the Font Generator:\n"
        "1. **To generate text in a specific font**, use the command `.font <your text> <font number>`.\n"
        "    - Example: `.font CyberNexus 1`\n\n"
        "2. **Available Fonts**:\n"
        "    - 1: `Tʜɪs`\n"
        "    - 2: `c̑̈y̑̈b̑̈ȇ̈ȓ̈n̑̈ȇ̈x̑̈ȗ̈s̑̈`\n"
        "    - 3: `c̆̈y̆̈b̆̈ĕ̈r̆̈n̆̈ĕ̈x̆̈ŭ̈s̆̈`\n"
        "    - 4: `༙c༙y༙b༙e༙r༙n༙e༙x༙u༙s༙`\n"
        "    - 5: `🄲🅈🄱🄴🅁🄽🄴🅇🅄🅂`\n"
        "    - 6: `𝖼𝓎𝒷𝑒𝓇𝓃𝑒𝓍𝓊𝓈`\n"
        "    - 7: `𝓬𝔂𝓫𝓮𝓻𝓷𝓮𝓍𝓾𝓼`\n"
        "    - 8: `𝒸𝓎𝒷𝑒𝓇𝓃𝑒𝓍𝓊𝓈`\n\n"
        "3. **Example usage**: `.font CyberNexus 1` to see the text in the first font.\n"
        "4. If you don't provide a number, the bot will show the text in all fonts.\n"
        "**Enjoy transforming your text!** 💫"
    )
