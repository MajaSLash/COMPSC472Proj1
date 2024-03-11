import os
import threading
import multiprocessing
import queue
import psutil
import signal
import time
from collections import Counter

class ProcessManager:
    def __init__(self):
        self.processes = {}

    def list_processes(self):
        """List all running processes"""
        self.processes = {}
        for proc in psutil.process_iter():
            self.processes[proc.pid] = proc
        return self.processes

    def kill_process(self, pid):
        """Kill a process by its PID"""
        try:
            os.kill(pid, signal.SIGKILL)
            del self.processes[pid]
            return True
        except:
            return False

    def suspend_process(self, pid):
        """Suspend a process by its PID"""
        try:
            os.kill(pid, signal.SIGSTOP)
            return True
        except:
            return False

    def resume_process(self, pid):
        """Resume a suspended process by its PID"""
        try:
            os.kill(pid, signal.SIGCONT)
            return True
        except:
            return False
class ThreadManager:
    def __init__(self):
        self.threads = {}

    def list_threads(self, pid):
        """List all threads associated with a process"""
        self.threads = {}
        try:
            process = psutil.Process(pid)
            for thread in process.threads():
                self.threads[thread.id] = thread
            return self.threads
        except psutil.NoSuchProcess:
            return None

    def kill_thread(self, tid):
        """Kill a thread by its TID"""
        try:
            os.kill(tid, signal.SIGKILL)
            del self.threads[tid]
            return True
        except:
            return False
        
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
        print("CPU Utilization: {}%".format(cpu_percent))
        print("Memory Utilization: {}%".format(memory_info.percent))
        time.sleep(5)

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

def load_and_distribute_file(filename, num_segments):
    file_size = os.path.getsize(filename)
    segment_size = file_size // num_segments
    segments = []

    with open(filename, 'r') as file:
        for _ in range(num_segments):
            segment = file.read(segment_size)
            segments.append(segment)

    return segments

def process_segment(segment, results_queue):
    # Convert characters to uppercase
    segment_uppercase = segment.upper()

    # Count occurrences of each character
    char_count = Counter(segment_uppercase)

    # Send results to the results queue
    results_queue.put(char_count)

def process_parallel(filename, num_segments, num_processes):
    segments = load_and_distribute_file(filename, num_segments)
    results_queue = multiprocessing.Queue()

    # Create processes to process each segment
    processes = []
    for segment in segments:
        p = multiprocessing.Process(target=process_segment, args=(segment, results_queue))
        processes.append(p)
        p.start()

    # Join processes
    for p in processes:
        p.join()

    # Combine results from the queue
    final_result = Counter()
    while not results_queue.empty():
        final_result += results_queue.get()

    return final_result

def main():
    process_manager = ProcessManager()
    thread_manager = ThreadManager()

    process_manager = ProcessManager()
    thread_manager = ThreadManager()

    monitor_thread = threading.Thread(target=monitor_system)
    monitor_thread.daemon = True
    monitor_thread.start()

    # Process IPC - Shared Memory
    shared_value = multiprocessing.Value('i', 0)

    # Process IPC - Message Passing
    message_queue = multiprocessing.Queue()

    # Thread IPC - Shared Memory
    lock = threading.Lock()
    shared_variable = multiprocessing.Value('i', 0)

    # Thread IPC - Message Passing
    message_queue_thread = queue.Queue()

    while True:
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

        choice = input("Enter your choice: ")

        if choice == '1':
            processes = process_manager.list_processes()
            for pid, proc in processes.items():
                print_process_info(proc)

        elif choice == '2':
            pid = int(input("Enter PID of the process to kill: "))
            if process_manager.kill_process(pid):
                print("Process with PID {} killed successfully.".format(pid))
            else:
                print("Failed to kill process.")

        elif choice == '3':
            pid = int(input("Enter PID of the process to suspend: "))
            if process_manager.suspend_process(pid):
                print("Process with PID {} suspended successfully.".format(pid))
            else:
                print("Failed to suspend process.")

        elif choice == '4':
            pid = int(input("Enter PID of the process to resume: "))
            if process_manager.resume_process(pid):
                print("Process with PID {} resumed successfully.".format(pid))
            else:
                print("Failed to resume process.")

        elif choice == '5':
            pid = int(input("Enter PID of the process to list threads: "))
            threads = thread_manager.list_threads(pid)
            if threads:
                for tid, thread in threads.items():
                    print_thread_info(thread)
            else:
                print("No such process found.")

        elif choice == '6':
            tid = int(input("Enter TID of the thread to kill: "))
            if thread_manager.kill_thread(tid):
                print("Thread with TID {} killed successfully.".format(tid))
            else:
                print("Failed to kill thread.")

        elif choice == '7':
            process_ipc_shared_memory(shared_value)
            print("Shared memory value after increment: ", shared_value.value)

        elif choice == '8':
            process_ipc_message_passing(message_queue)
            message = message_queue.get()
            print("Received message in process: ", message)

        elif choice == '9':
            thread_ipc_shared_memory(lock, shared_variable)
            print("Shared memory value after increment: ", shared_variable.value)

        elif choice == '10':
            thread_ipc_message_passing(message_queue_thread)
            message = message_queue_thread.get()
            print("Received message in thread: ", message)
        elif choice == '11':
            filename = input("Enter the path to the large text file: ")
            num_segments = int(input("Enter the number of segments to split the file into: "))
            num_processes = int(input("Enter the number of processes to use: "))

            start_time = time.time()
            result = process_parallel(filename, num_segments, num_processes)
            end_time = time.time()

            print("Results:")
            print(result)
            print("Time taken: {} seconds".format(end_time - start_time))

        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()