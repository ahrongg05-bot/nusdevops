# Store the name of the log file in a variable.
log_file = "deployment.log"

# Open the log file in write ('w') mode.
# If the file does not exist, Python creates it.
# If it already exists, Python erases its previous contents.
with open(log_file, 'w') as f:

    # Write the first line (header) into the log file.
    # \n means move to the next line.
    f.write("Deployment Log Start =\n")

# Create a list of servers that will be deployed.
servers = ["web01", "web02", "db01"]

# Loop through each server in the list one by one.
for server in servers:

    # Open the same log file in append ('a') mode.
    # Append mode adds new text without deleting existing contents.
    with open(log_file, 'a') as f:

        # Write which server is currently being deployed.
        # f-string inserts the value of 'server'.
        # \n creates a new line.
        f.write(f"Deploying to {server}...\n")

        # Write a success message for that server.
        f.write(f"{server} deployment successful.\n")

# Print a blank line followed by a heading on the screen.
print("\nReading log contents:")

# Open the log file in read ('r') mode.
with open(log_file, 'r') as f:

    # Read the entire contents of the file into the variable 'content'.
    content = f.read()

    # Display everything stored in the log file.
    print(content)