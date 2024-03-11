from process_manager import *
from thread_manager import *
from utils import *
from file_processing import *

import threading
import multiprocessing
import queue

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
        display_menu()
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
            process_large_text_file()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()