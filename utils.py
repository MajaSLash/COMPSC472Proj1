import psutil
import time
import random
import string


def display_menu():
    print("\n1. List Processes")
    print("2. Kill Process")
    print("3. Suspend Process")
    print("4. Resume Process")
    print("5. List Threads for Process")
    print("6. Kill Thread")
    print("7. Process IPC (Shared Memory)")
    print("8. Process IPC (Message Passing)")
    print("9. Thread IPC (Shared Memory)")
    print("10. Thread IPC (Message Passing)")
    print("11. Process Large Text File")
    print("0. Exit")

def print_process_info(process_info):
    print("PID: ", process_info.pid)
    print("Name: ", process_info.name())
    print("Status: ", process_info.status())
    print("Parent PID: ", process_info.ppid())
    print("Username: ", process_info.username())
    print("Memory Info: ", process_info.memory_info())

def print_thread_info(thread_info):
    print("TID: ", thread_info.id)
    print("Thread Name: ", thread_info.name)
    print("Thread Status: ", thread_info.status)

def monitor_system():
    while True:
        # System-wide resource utilization monitoring
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        print("System-wide resource utilization monitoring (This will repeat every 30 seconds)")
        print("CPU Utilization: {}%".format(cpu_percent))
        print("Memory Utilization: {}%".format(memory_info.percent))
        time.sleep(30)

def process_ipc_shared_memory(value):
    print("Process: Incrementing shared memory value")
    value.value += 1

def process_ipc_message_passing(queue):
    print("Process: Sending message through queue")
    queue.put("Hello from process")

def thread_ipc_shared_memory(lock, shared_variable):
    print("Thread: Incrementing shared memory value")
    with lock:
        shared_variable.value += 1

def thread_ipc_message_passing(queue):
    print("Thread: Sending message through queue")
    queue.put("Hello from thread")

def generate_sample_text_file():
    filename = "sample_text_file.txt"
    num_lines = 10000  # Adjust as needed
    line_length = 100  # Adjust as needed
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            line = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=line_length))
            file.write(line + '\n')
