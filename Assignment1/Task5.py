import os
def cpu_task():
    x = 0
    # Simple CPU-intensive loop
    for i in range(10**7):
        x += i % 2
    print(f"Process PID={os.getpid()} finished.")
# Different nice values for processes
nice_values = [0, 5, 10]
for val in nice_values:
    pid = os.fork()

    if pid == 0:   # Child process
        os.nice(val)   # Set process priority
        print(f"Child PID={os.getpid()}, Nice={val}, Parent PID={os.getppid()}")
        cpu_task()
        os._exit(0)
# Parent waits for all children
for _ in nice_values:
    os.wait()
