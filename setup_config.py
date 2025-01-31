import os

# Function to create or update config.py
def create_config():
    print("Welcome to CyberNexus setup!")

    # Ask for required data
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API HASH: ")
    string_session = input("Enter your STRING SESSION: ")
    deployer_name = input("Enter the deployer's name (e.g., Your Name): ")

    # Prepare config content
    config_content = f"""API_ID = {api_id}  # Replace with your actual API ID
API_HASH = "{api_hash}"  # Replace with your actual API hash
STRING_SESSION = "{string_session}"  # Replace with your actual string session

CMD_HNDLR = "."  # Command handler, '.' in your case

# Deployer Name
DEPLOYER_NAME = "{deployer_name}"  # Deployer's name
"""

    # Save the data to config.py
    with open("config.py", "w") as config_file:
        config_file.write(config_content)

    print("config.py has been successfully created with the provided details.")

# Run the setup function
if __name__ == "__main__":
    if not os.path.exists("config.py"):
        create_config()
    else:
        print("config.py already exists. You can edit it manually if required.")
