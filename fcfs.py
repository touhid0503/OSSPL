# Simple FCFS Scheduling Algorithm

def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calculate average waiting and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Display results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


# Example usage
processes = [1, 2, 3]  # Process IDs
burst_time = [10, 5, 8]  # Burst times of processes

fcfs(processes, burst_time)
