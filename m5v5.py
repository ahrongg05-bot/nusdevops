# Import the os module to access environment variables.
import os

# Import the subprocess module to run system commands.
# (Not used in this example, but useful for automation scripts.)
import subprocess

# Get the value of the environment variable BUILD_ID.
# If BUILD_ID does not exist, use "unknown" as the default value.
BUILD_ID = os.getenv("BUILD_ID", "unknown")

# Get the value of the environment variable API_TOKEN.
# Returns None if the variable does not exist.
# This is safer than hardcoding API keys in your code.
API_TOKEN = os.getenv("API_TOKEN")

# Print the current build ID.
print(f"Current Build ID: {BUILD_ID}")

# Check whether an API token exists.
if API_TOKEN:

    # If the token exists, print a confirmation message.
    # Do NOT print the actual token for security reasons.
    print("API token found (not displayed for security).")

# Otherwise...
else:

    # Inform the user that no API token was found.
    print("No API token found. Please set it in your environment.")