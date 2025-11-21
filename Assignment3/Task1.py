# PART 1: PRIORITY SCHEDULING
processes = []
n = int(input("Enter number of processes: "))
burst_times = []
# Input burst time and priority for each process
for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
    processes.append((i+1, bt, pr))
    burst_times.append(bt)
# Sort processes based on priority value 
processes.sort(key=lambda x: x[2])
wt = 0 
total_wt = 0 
total_tt = 0 
gantt_priority = []   # To store Gantt chart intervals
print("\nPriority Scheduling:")
print("PID\tBT\tPriority\tWT\tTAT")
# Generate waiting time, turnaround time and Gantt entries
for pid, bt, pr in processes:
    tat = wt + bt     # Turnaround time = waiting time + burst time
    print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
    total_wt += wt
    total_tt += tat
    gantt_priority.append((pid, wt, tat))  # (PID, start, end)
    wt += bt        # Increase waiting time for next process
# Display averages
print(f"\nAverage Waiting Time: {total_wt / n}")
print(f"Average Turnaround Time: {total_tt / n}")
# Print Gantt chart for Priority Scheduling
print("\nGantt Chart (Priority Scheduling):")
for pid, start, end in gantt_priority:
    print(f"| P{pid} ({start}-{end}) ", end="")
print("|\n")

# PART 2: ROUND ROBIN SCHEDULING
print("\n--- ROUND ROBIN SCHEDULING ---")
quantum = int(input("Enter Time Quantum: "))
remaining_bt = burst_times.copy()  
time = 0
waiting_time = [0] * n             # Waiting time per process
turnaround_time = [0] * n          # Turnaround time per process
gantt_rr = []                      # Gantt chart entries for RR
start_time_recorded = [False] * n  # For tracking first execution time
start_times = [0] * n              # First start time of each process
# Round Robin loop (continues until all processes finish)
while True:
    done = True
    for i in range(n):
        # Skip finished processes
        if remaining_bt[i] > 0:
            done = False
            # Record first time the process gets CPU
            if not start_time_recorded[i]:
                start_times[i] = time
                start_time_recorded[i] = True
            # Process executes for either full quantum or remaining time
            exec_time = min(quantum, remaining_bt[i])
            # Add to Gantt Chart
            gantt_rr.append((i+1, time, time + exec_time))
            time += exec_time            # Move global time forward
            remaining_bt[i] -= exec_time # Decrease remaining burst time
            # Process just finished
            if remaining_bt[i] == 0:
                turnaround_time[i] = time
                waiting_time[i] = turnaround_time[i] - burst_times[i]
    if done:   
        break
# Calculate averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
# Show Round Robin results
print("\nRound Robin Results:")
print("PID\tBT\tWT\tTAT")
for i in range(n):
    print(f"{i+1}\t{burst_times[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")
print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")
# Print Gantt chart for Round Robin
print("\nGantt Chart (Round Robin):")
for pid, start, end in gantt_rr:
    print(f"| P{pid} ({start}-{end}) ", end="")
print("|")
