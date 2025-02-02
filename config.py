import os
import sys
import time

# ASCII Banner
BANNER = r"""
.__   __.  __________   ___  __    __       _______.
|  \ |  | |   ____\  \ /  / |  |  |  |     /       |
|   \|  | |  |__   \  V  /  |  |  |  |    |   (----`
|  . `  | |   __|   >   <   |  |  |  |     \   \    
|  |\   | |  |____ /  .  \  |  `--'  | .----)   |   
|__| \__| |_______/__/ \__\  \______/  |_______/    
"""

# Cool Loading Animation
def loading_screen(message="Initializing Setup"):
    sys.stdout.write("\n")
    for _ in range(3):  # Three cycles of loading dots
        for dot in [".  ", ".. ", "..."]:
            sys.stdout.write(f"\r{message} {dot}")
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write("\r✔️ Setup Initialized Successfully!    \n\n")
    time.sleep(1)

# Input Function with Cool Arrow
def get_input(prompt):
    while True:
        user_input = input(f"➤ {prompt}: ").strip()
        if user_input:
            return user_input
        print("⚠️ This field cannot be empty. Please enter a valid value.")

# Clear Screen Before Displaying Banner
os.system("clear" if os.name == "posix" else "cls")

# Display Banner & Loading
print(BANNER)
loading_screen("\n🚀 Loading CyberNexus Setup")

print("🚀 Welcome to CyberNexus Userbot Configuration 🚀\n")

api_id = get_input("Enter your API ID")
api_hash = get_input("Enter your API HASH")
string_session = get_input("Enter your STRING SESSION")
cmd_hndlr = get_input("Enter your Command Handler")
deployer_name = get_input("Enter your Deployer Name")

# Creating the Configuration File
config_content = f'''# CyberNexus Userbot Configuration

API_ID = {api_id}
API_HASH = "{api_hash}"
STRING_SESSION = "{string_session}"
CMD_HNDLR = "{cmd_hndlr}"
DEPLOYER_NAME = "{deployer_name}"
'''

with open("config.py", "w") as config_file:
    config_file.write(config_content)

# Final Success Message with Loading Effect
loading_screen("Saving Configuration")
print("✅ Configuration saved successfully in 'config.py'! 🚀\n")

# Auto-Start CyberNexus Userbot
print("🔄 Starting CyberNexus Userbot\n")
loading_screen("Wait few Seconds..")
time.sleep(2)  # Small delay before execution
os.system("python cybernexus.py")
