# Import the subprocess module.
# This module allows Python to run external system commands.
import subprocess

# Run the system command "ping google.com".
# subprocess.run() executes the command and waits until it finishes.
result = subprocess.run(

    # The command is provided as a list.
    # "ping" is the program to execute.
    # "google.com" is the argument passed to the ping command.
    ["ping","-c", "4", "google.com"], #ADD -C (COUNT) , 4 times or pings

    # Capture the command's standard output (stdout)
    # instead of printing it directly to the terminal.
    capture_output=True,

    # Return the output as normal text (string)
    # instead of raw bytes.
    text=True
)

# Print everything the command wrote to standard output.
# For ping, this is usually the ping results.
print("STDOUT:\n", result.stdout)

# Print everything the command wrote to standard error.
# This is useful for debugging if the command fails.
print("STDERR:\n", result.stderr)

# Print the exit code of the command.
# 0 usually means success.
# Any non-zero value usually indicates an error.
print(f"Exit Code: {result.returncode}")

# Print the command (arguments) that was executed.
print(f"Command Executed: {result.args}")