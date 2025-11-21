def allocate_memory(strategy):
    # Input memory partitions
    partitions = list(map(int, input("Enter partition sizes: ").split()))
    # Input process sizes to be allocated
    processes = list(map(int, input("Enter process sizes: ").split()))
    allocation = [-1] * len(processes)
    # Allocation Logic (same logic you provided, only commented)
    for i, psize in enumerate(processes):   # For each process
        idx = -1                            # Index of selected partition
        # FIRST FIT STRATEGY
        if strategy == "first":
            for j, part in enumerate(partitions):
                if part >= psize:           # First partition large enough
                    idx = j
                    break
        # BEST FIT STRATEGY
        elif strategy == "best":
            best_fit = float("inf")
            for j, part in enumerate(partitions):
                if part >= psize and part < best_fit:
                    best_fit = part
                    idx = j
        # WORST FIT STRATEGY
        elif strategy == "worst":
            worst_fit = -1
            for j, part in enumerate(partitions):
                if part >= psize and part > worst_fit:
                    worst_fit = part
                    idx = j
        # If a suitable partition is found
        if idx != -1:
            allocation[i] = idx
            partitions[idx] -= psize 
    # Output Allocation Results
    print(f"\n{strategy.upper()} FIT ALLOCATION:")
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} cannot be allocated")
allocate_memory("first")
allocate_memory("best")
allocate_memory("worst")
