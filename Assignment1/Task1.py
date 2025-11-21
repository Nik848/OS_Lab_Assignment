import os

N = 3   # number of child processes

for i in range(N):
    pid = os.fork()

    if pid == 0:     # Child process
        print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}, Message=Hello")
        os._exit(0)   # exit child so it doesn't create more children

# Parent waits for all children
for _ in range(N):
    os.wait()
