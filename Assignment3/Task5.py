# MFT: Fixed Partition Memory Management
def MFT():
    mem_size = int(input("Enter total memory size: "))
    part_size = int(input("Enter partition size: "))
    n = int(input("Enter number of processes: "))
    # Number of fixed partitions that can be created
    partitions = mem_size // part_size
    print(f"Memory divided into {partitions} partitions of size {part_size} each.")
    # For each process, check if it fits in a partition
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))

        if psize <= part_size:
            print(f"Process {i+1} allocated in a fixed partition.")
        else:
            print(f"Process {i+1} too large for the fixed partition.")
# MVT: Variable Partition Memory Management
def MVT():
    mem_size = int(input("Enter total memory size: "))
    n = int(input("Enter number of processes: "))
    # For each process, allocate memory if enough space remains
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))

        if psize <= mem_size:
            print(f"Process {i+1} allocated with {psize} memory.")
            mem_size -= psize   # Reduce available memory
        else:
            print(f"Process {i+1} cannot be allocated. Not enough memory.")
# MAIN EXECUTION
print("MFT Simulation:")
MFT()
print("\nMVT Simulation:")
MVT()
