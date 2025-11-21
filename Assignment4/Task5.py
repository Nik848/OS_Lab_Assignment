def fcfs(processes):
    # processes = [(pid, burst_time)]
    wt = [0] * len(processes)
    tat = [0] * len(processes)

    # Waiting Time calculation
    for i in range(1, len(processes)):
        wt[i] = wt[i-1] + processes[i-1][1]

    # Turn Around Time
    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i][1]

    print("\nFCFS Scheduling")
    print("PID\tBT\tWT\tTAT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{wt[i]}\t{tat[i]}")



def sjf(processes):
    # processes = [(pid, burst_time)]
    # Sort by burst time
    processes.sort(key=lambda x: x[1])

    wt = [0] * len(processes)
    tat = [0] * len(processes)

    # Waiting time
    for i in range(1, len(processes)):
        wt[i] = wt[i-1] + processes[i-1][1]

    # Turn around time
    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i][1]

    print("\nSJF Scheduling")
    print("PID\tBT\tWT\tTAT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{wt[i]}\t{tat[i]}")

def priority_sched(processes):
    # processes = [(pid, burst_time, priority)]
    # Lower priority value = higher priority
    processes.sort(key=lambda x: x[2])

    wt = [0] * len(processes)
    tat = [0] * len(processes)

    for i in range(1, len(processes)):
        wt[i] = wt[i-1] + processes[i-1][1]

    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i][1]

    print("\nPriority Scheduling")
    print("PID\tBT\tPR\tWT\tTAT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{wt[i]}\t{tat[i]}")

def round_robin(processes, quantum):
    # processes = [(pid, burst_time)]
    rem_bt = [p[1] for p in processes]
    wt = [0] * len(processes)
    t = 0  # current time

    while True:
        done = True
        for i in range(len(processes)):
            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i][1]
                    rem_bt[i] = 0

        if done:
            break

    tat = [wt[i] + processes[i][1] for i in range(len(processes))]

    print("\nRound Robin Scheduling")
    print("PID\tBT\tWT\tTAT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{wt[i]}\t{tat[i]}")

if __name__ == "__main__":

    # FCFS / SJF / RR input → (PID, BT)
    procs1 = [(1, 6), (2, 8), (3, 7), (4, 3)]
    # Priority input → (PID, BT, PRIORITY)
    procs2 = [(1, 10, 3), (2, 1, 1), (3, 2, 4), (4, 1, 2)]
    fcfs(procs1.copy())
    sjf(procs1.copy())
    priority_sched(procs2.copy())
    round_robin(procs1.copy(), quantum=2)
