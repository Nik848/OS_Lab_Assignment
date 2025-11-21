total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks
# Number of files to allocate
n = int(input("Enter number of files: "))
# FILE ALLOCATION PROCESS
for i in range(n):
    # Input starting block number for file
    start = int(input(f"Enter starting block for file {i+1}: "))
    # Input how many continuous blocks the file needs
    length = int(input(f"Enter length of file {i+1}: "))
    allocated = True  # Assume allocation is possible
    # Check if all required blocks are free and within limit
    for j in range(start, start + length):
        # Out-of-range OR already allocated
        if j >= total_blocks or block_status[j] == 1:
            allocated = False
            break
    # ALLOCATE IF POSSIBLE
    if allocated:
        # Mark the blocks as allocated
        for j in range(start, start + length):
            block_status[j] = 1
        print(f"File {i+1} allocated from block {start} to {start + length - 1}")
    # DEALLOCATION FAILED
    else:
        print(f"File {i+1} cannot be allocated.")
