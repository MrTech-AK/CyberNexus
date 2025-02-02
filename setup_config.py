# setup_config.py
import os

BANNER = """
╔══════════════════════════════════════════════╗
║                CYBERNEXUS SETUP CONFIG           
╠══════════════════════════════════════════════╣
║         Configure your Userbot and Bot easily   
╚══════════════════════════════════════════════╝
"""

PROMPT_STYLE = "\033[1;32m=>\033[0m"  # Green arrow for prompts


def collect_input(prompt):
    """Helper function to collect input with a stylized prompt."""
    return input(f"{PROMPT_STYLE} {prompt}: ").strip()


def main():
    print(BANNER)

    print("\nWelcome to the CyberNexus Configuration Setup!")
    print("Please enter the following details to set up your Userbot and Bot.\n")

    # Collect user inputs
    api_id = collect_input("Enter your Telegram API ID")
    api_hash = collect_input("Enter your Telegram API HASH")
    string_session = collect_input("Enter your STRING_SESSION (Use Telethon String Session generator)")
    cmd_prefix = collect_input("Enter your preferred Command Prefix (e.g., '.' or '/')")
    telegram_username = collect_input("Enter your Telegram Username (with '@')")
    telegram_name = collect_input("Enter your Telegram Display Name")

    # Create config.py
    config_content = f"""
# CyberNexus Configuration File

API_ID = {api_id}
API_HASH = "{api_hash}"
STRING_SESSION = "{string_session}"
CMD_PREFIX = "{cmd_prefix}"
TELEGRAM_USERNAME = "{telegram_username.strip('@')}"  # Username without '@'
TELEGRAM_NAME = "{telegram_name}"

# Log group ID will be added automatically after startup.py
LOG_CHAT_ID = None
BOT_TOKEN = None  # Will be generated automatically by cybernexus.py
"""

    # Write to config.py
    with open("config.py", "w") as config_file:
        config_file.write(config_content.strip())
    
    print("\nConfiguration saved to \033[1mconfig.py\033[0m successfully!")
    print("You can now run \033[1mpython cybernexus.py\033[0m to initialize CyberNexus.\n")


if __name__ == "__main__":
    main()
