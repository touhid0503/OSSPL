process=[1,2,3]
bt=[10,5,8]
n=len(process)

print("Process: ")
for i in range(n):
    print(process[i])

print("Burst Time: ")
for i in range(n):
    print(bt[i])
    
wt=[0]*n
tat=[0]*n

print("Waiting Time: ")
print(wt[0])
for i in range(1,n):
    wt[i]=wt[i-1]+bt[i-1]
    print(wt[i])

print("Total Arround Time: ")
for i in range(n):
    tat[i]=bt[i]+wt[i]
    print(tat[i])

awt=sum(wt)/n
atat=sum(tat)/n

print("Average Waiting Time: ")
print(awt)
print("Average Total Arround Time: ")
print(atat)

