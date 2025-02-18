import time
from multiprocessing import Process

# Define the target function for the process
def my_process():
    print("Process started.")
    time.sleep(10)  # Simulate a task that takes time
    print("Process finished.")

# Create a process
process = Process(target=my_process)

# Start the process
process.start()

# Optionally, you can wait for some time before terminating
time.sleep(2)  # Let the process run for 2 seconds

# Terminate the process
print("Terminating the process.")
process.terminate()

# Wait for the process to end (this is important to ensure the process ends properly)
process.join()

print("Process terminated.")
