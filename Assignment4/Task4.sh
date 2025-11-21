#!/bin/bash
# Print the kernel version
echo "Kernel Version:"
uname -r
# Print the current logged-in user
echo "User:"
whoami
# Print hardware / virtualization details
echo "Hardware Info:"
lscpu | grep 'Virtualization'
