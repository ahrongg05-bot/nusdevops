#!/bin/bash

echo "Hostname: $(hostname)"
echo "Current User: $(whoami)"
echo "Kernel Version:"
uname -r
#uname -r
#-r = Show the kernel release/version.

echo "Memory Usage:"
free -h
# free → Shows RAM (memory) usage.
# -h = Human-readable format (KB, MB, GB instead of huge numbers).


echo "Disk Usage:"
df -h
#df = Disk Filesystem.
#Shows storage usage of your hard drive.
#-h = Human-readable sizes.