import os
import time

pid = os.fork()

if pid == 0:   # Child process
    print(f"Child: PID={os.getpid()}, Parent PID={os.getppid()}")
    os._exit(0)   # Child exits immediately → becomes a zombie until parent waits

else:          # Parent process
    print(f"Parent: PID={os.getpid()}, Child PID={pid}")
    
    # Parent does NOT call wait()
    # This keeps the child in 'Z' state (zombie) until the parent exits
    print("Child will become a zombie. Run 'ps -l' in another terminal.")
    
    time.sleep(20)   # Keep parent alive so zombie is visible in process table
