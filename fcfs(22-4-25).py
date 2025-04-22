print("Enter the length: ")
n=int(input())

process=[]
print("Enter Processes: ")
for i in range(n):
    z=int(input())
    process.append(z)

bt=[]
print("Enter Burst Times: ")
for i in range(n):
    z=int(input())
    bt.append(z)

wt=[0]*n
tat=[0]*n

for i in range(1,n):
    wt[i]=bt[i-1]+wt[i-1]
    
for i in range(n):
    tat[i]=bt[i]+wt[i]
    
print(f"{'PID':<5} {'Burst Time':<12} {'Waiting Time':<15} {'Turnaround Time':<18}")
for i in range(n):
    print(f"{process[i]:<5} {bt[i]:<12} {wt[i]:<15} {tat[i]:<18}")

awt=sum(wt)/n
print("Average Waiting Time: ",awt)
atat=sum(tat)/n
print("Average Total Arround Time: ",atat)