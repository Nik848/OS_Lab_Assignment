import os
# Create a pipe: r = read end, w = write end
r, w = os.pipe()
pid = os.fork()
if pid > 0:
    # Parent process
    os.close(r)  # close unused read end in parent
    msg = b"Hello from parent\n"
    os.write(w, msg)  # write to pipe
    os.close(w)       # close write end to send EOF to child

    # Wait for child to finish and reap it (avoid zombie)
    os.waitpid(pid, 0)
    print("Parent: child has terminated.")

else:
    # Child process
    os.close(w)  # close unused write end in child
    # Read up to 1024 bytes from the pipe
    data = os.read(r, 1024)
    os.close(r)
    print("Child received:", data.decode(), end='')  # decode and print
