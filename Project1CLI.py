import COMPSC472Proj1.Project1Sys as Project1Sys

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

def process_large_text_file():
    filename = input("Enter the path to the large text file: ")
    num_segments = int(input("Enter the number of segments to split the file into: "))
    num_processes = int(input("Enter the number of processes to use: "))

    start_time = Project1Sys.time.time()
    result = Project1Sys.process_parallel(filename, num_segments, num_processes)
    end_time = Project1Sys.time.time()

    print("Results:")
    print(result)
    print("Time taken: {} seconds".format(end_time - start_time))

def main():
    process_manager = Project1Sys.ProcessManager()
    thread_manager = Project1Sys.ThreadManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            processes = process_manager.list_processes()
            for pid, proc in processes.items():
                Project1Sys.print_process_info(proc)

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
                    Project1Sys.print_thread_info(thread)
            else:
                print("No such process found.")

        elif choice == '6':
            tid = int(input("Enter TID of the thread to kill: "))
            if thread_manager.kill_thread(tid):
                print("Thread with TID {} killed successfully.".format(tid))
            else:
                print("Failed to kill thread.")

        elif choice == '7':
            Project1Sys.process_ipc_shared_memory(Project1Sys.shared_value)
            print("Shared memory value after increment: ", Project1Sys.shared_value.value)

        elif choice == '8':
            Project1Sys.process_ipc_message_passing(Project1Sys.message_queue)
            message = Project1Sys.message_queue.get()
            print("Received message in process: ", message)

        elif choice == '9':
            Project1Sys.thread_ipc_shared_memory(Project1Sys.lock, Project1Sys.shared_variable)
            print("Shared memory value after increment: ", Project1Sys.shared_variable.value)

        elif choice == '10':
            Project1Sys.thread_ipc_message_passing(Project1Sys.message_queue_thread)
            message = Project1Sys.message_queue_thread.get()
            print("Received message in thread: ", message)
        elif choice == '11':
            process_large_text_file()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
