##automation.py
#part1
# cd the folder then #touch .env
# ls -a to check if .env is created
#nano .env to edit and ctrl x to exit and save
#BUILD_ID=1.0
# API_TOKEN=your_dummy_token
# python3 -m venv venv create virtual environment
# source venv/bin/activate to activate virtual environment

import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

# Read the variables
build_id = os.getenv("BUILD_ID")
api_token = os.getenv("API_TOKEN")

print("===== Part 1: Environment Configuration =====")
print(f"Build ID: {build_id}")

if api_token:
    print("API token exists.")
else:
    print("API token does not exist.")


#part2
print("\n===== Part 2: Server Health Check =====")
servers = ["web01", "web02"] # create list of servers to check

#create dictionary to store server health status #keys"value

server_health = {
    "web01": "ok",
    "web02": "failed"
}

# loop
for server in servers:
    if server_health[server] == "ok":
        print(f"{server} is healthy")
    else:
        print(f"{server} has failed")



print("\n===== Part 3: File Logging =====")

# Create the log file and write the header # "w" creates or overwrites the file.
with open("deployment.log", "w") as log_file:
    log_file.write("Deployment Log Start\n")

# Append deployment messages for each server #with open("deployment.log", "a") as log_file:
with open("deployment.log", "a") as log_file:
    for server in servers:
        log_file.write(f"Deploying to {server}\n")
        log_file.write(f"{server} deployment successful\n")

# Read and print the file content #"r" reads the file.
with open("deployment.log", "r") as log_file:
    content = log_file.read()

print(content)

#part4
import subprocess

print("\n===== Part 4: System Command Execution =====")

# Run a ping command
result = subprocess.run(
    ["ping", "-c", "1", "127.0.0.1"],
    capture_output=True,
    text=True
)

# Print the command results
print("Output:")
print(result.stdout)

print("Error:")
print(result.stderr)

print("Return code:")
print(result.returncode)

#p5
import requests
print("\n===== Part 5: API Automation =====")

# Public API URL
url = "https://jsonplaceholder.typicode.com/todos/1"

# Send GET request
response = requests.get(url)

# Print the status code
print("Status Code:")
print(response.status_code)

# Print the JSON response
print("Response Snippet:")
print(response.json())