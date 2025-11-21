# Total number of physical disk blocks
total_blocks = int(input("Enter total number of blocks: "))
# 0 → free block
# 1 → allocated block
block_status = [0] * total_blocks
# Number of files to simulate
n = int(input("Enter number of files: "))
# FILE ALLOCATION PROCESS
for i in range(n):
    # Ask for index block of current file
    index = int(input(f"Enter index block for file {i+1}: "))
    # Check if index block is already used
    if block_status[index] == 1:
        print("Index block already allocated.")
        continue
    # Number of data blocks needed
    count = int(input("Enter number of data blocks: "))
    # User enters block numbers separated by spaces
    data_blocks = list(map(int, input("Enter block numbers: ").split()))
    # Validate:
    # 1. Count matches number of blocks given
    # 2. No data block is already allocated
    if len(data_blocks) != count or any(block_status[blk] == 1 for blk in data_blocks):
        print("Block(s) already allocated or invalid input.")
        continue
    # ALLOCATE INDEX BLOCK AND DATA BLOCKS
    block_status[index] = 1 
    # Allocate all data blocks
    for blk in data_blocks:
        block_status[blk] = 1
    # Print successful allocation
    print(f"File {i+1} allocated with index block {index} -> {data_blocks}")
