def priority_scheduling(processes):
    n = len(processes)
    
    # Sort processes based on priority (ascending order: lower priority number means higher priority)
    processes.sort(key=lambda x: x[2])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    # Print the process details
    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Calculate and print average waiting time and turnaround time
    avg_wait = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")

# Example process list: (Process ID, Burst Time, Priority)
process_list = [(1, 6, 2), (2, 8, 1), (3, 7, 3), (4, 3, 4)]
priority_scheduling(process_list)
