import os
# List of commands for children to execute
commands = [
    ["ls", "-l"],
    ["date"],
    ["ps"]
]
N = len(commands)
for i in range(N):
    pid = os.fork()

    if pid == 0:   # Child process
        print(f"\nChild {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}, executing {commands[i][0]}")
        
        # Replace child process with given command
        os.execvp(commands[i][0], commands[i])

        # If exec fails
        os._exit(1)

# Parent waits for all children to finish
for _ in range(N):
    os.wait()
