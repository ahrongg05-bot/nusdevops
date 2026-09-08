# Import the psutil module.
# psutil allows Python to retrieve information about CPU, memory,
# disk, network, and running processes.
import psutil

# Set the maximum allowed CPU usage (70%).
# If CPU usage is below this value, it is considered acceptable.
CPU_MAX = 70.0

# Set the minimum available memory.
# 512 * 1024**2 converts 512 MB into bytes.
MEM_MIN = 512 * 1024**2

# Define a function that checks whether system resources are sufficient.
def resources_ok():

    # Measure the current CPU usage.
    # interval=0.5 means psutil samples CPU usage over 0.5 seconds.
    cpu = psutil.cpu_percent(interval=0.5)

    # Get information about the system's virtual memory.
    # The returned object contains total, available, used, percent, etc.
    mem = psutil.virtual_memory()

    # Print the current CPU usage and available memory.
    # mem.available is in bytes, so divide by 1024**2 to convert to MB.
    print(
        f"[RESOURCES] CPU={cpu:.1f}% "
        f"AvailableMem={mem.available / 1024**2:.0f}MB"
    )

    # Return True only if BOTH conditions are met:
    # 1. CPU usage is below 70%.
    # 2. Available memory is greater than 512 MB.
    return cpu < CPU_MAX and mem.available > MEM_MIN



## ADD TO SEE THE RESULT 
# Call the function
result = resources_ok()

# Print whether resources are sufficient
print("Resources OK:", result)