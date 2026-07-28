import subprocess
import time

# Command to run
cmd = ["ping", "-c", "4", "google.com"]

# Maximum number of retries
retries = 3

# Timeout in seconds
timeout = 5

# Wait 2 seconds before retrying
delay = 2

attempt = 0
############################################# ABOVE MENTIONED NOT ADDED 

# Start counting retry attempts from 0.
attempt = 0

# Keep trying while the number of attempts is less than or equal to
# the maximum number of retries.
while attempt <= retries:

    # Try to execute the command.
    try:

        # Run the system command stored in the variable 'cmd'.
        result = subprocess.run(

            # The command to execute (e.g. ["ping", "-c", "4", "google.com"]).
            cmd,

            # Save the command's output instead of printing it.
            capture_output=True,

            # Return the output as text (string) instead of bytes.
            text=True,

            # Stop the command if it takes longer than 'timeout' seconds.
            timeout=timeout
        )

        # If the command produced any error output, print it.
        if result.stderr:
            print(result.stderr.strip())

        # Check whether the command finished successfully.
        # Exit code 0 means success.
        if result.returncode == 0:

            # Display a success message.
            print("Success\n")

        # Otherwise, the command failed.
        else:

            # Print the command's exit code.
            print(f"{result.returncode}")

    # This block runs if the command exceeds the timeout limit.
    except subprocess.TimeoutExpired as e:

        # Inform the user that the command timed out.
        print(f"[RESULT] TimeoutExpired after {timeout}s")

        # If any partial standard output was produced before timing out,
        # display it.
        if e.stdout:
            print("[STDOUT partial]\n" + e.stdout.strip())

        # If any partial error output was produced before timing out,
        # display it.
        if e.stderr:
            print("[STDERR partial]\n" + e.stderr.strip())

        # Increase the retry counter by one.
        attempt += 1

        # If there are still retries remaining...
        if attempt <= retries:

            # Tell the user we will wait before retrying.
            print(f"[RETRY] Sleeping {delay}s before retry...")

            # Pause the program for 'delay' seconds.
            time.sleep(delay)