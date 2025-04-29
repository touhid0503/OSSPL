def sjf_scheduling(processes):
    n = len(processes)
    
    processes.sort(key=lambda x: x[1])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    avg_wait = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")

process_list = [(1, 6), (2, 8), (3, 7), (4, 3)]
sjf_scheduling(process_list)
