import threading

counter = 5 

def increment():
    global counter
    for _ in range(1):  
        counter += 1  

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final counter value:", counter)
