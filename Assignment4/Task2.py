import multiprocessing
import logging
import time
# Configure the log file and format
logging.basicConfig(filename='system_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(processName)s - %(message)s')
# Function executed by each process
def process_task(name):
    logging.info(f"{name} started")   # Log process start
    time.sleep(2)                     # Simulate work
    logging.info(f"{name} terminated") # Log process end
if __name__ == '__main__':
    print("System Booting...")
    # Create two processes
    p1 = multiprocessing.Process(target=process_task, args=("Process-1",))
    p2 = multiprocessing.Process(target=process_task, args=("Process-2",))
    # Start processes
    p1.start()
    p2.start()
    # Wait for both to finish
    p1.join()
    p2.join()
    print("System Shutdown.")
