import qrcode
import io
from telethon import events
from cybernexus import client
import platform

@client.on(events.NewMessage(pattern=r"^\.qr (.+)$", outgoing=True))
async def generate_qr(event):
    """Generates a QR code from given text."""
    text = event.pattern_match.group(1)

    # Creating QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Save to memory
    img = qr.make_image(fill="black", back_color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    await event.reply("✅ **QR Code Generated:**", file=img_bytes)
    await event.edit("⚡ Powered By CyberNexus")
