import os
pid = input("Enter PID: ").strip()
# Process details
with open(f"/proc/{pid}/status") as f:
    for line in f:
        if line.startswith("Name:") or line.startswith("State:") or line.startswith("VmRSS:"):
            print(line.strip())
# Executable path
try:
    print("Executable:", os.readlink(f"/proc/{pid}/exe"))
except PermissionError:
    print("Executable: [Permission Denied]")
# Open file descriptors
try:
    print("Open FDs:", os.listdir(f"/proc/{pid}/fd"))
except PermissionError:
    print("Open FDs: [Permission Denied]")