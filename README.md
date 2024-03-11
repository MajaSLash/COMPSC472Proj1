# COMPSC472Proj1
Repo for Project 1 of COMPSC 472

## Description of the project:

The project aims to create a multi-process and multi-thread task manager with additional features for parallel text file processing. It provides functionalities to manage processes and threads, including listing processes/threads, killing processes/threads, suspending/resuming processes, and more. Additionally, it allows users to process large text files efficiently using parallelization techniques, such as multiprocessing.

## Structure with diagram and descriptions:

plaintext
Copy code
text_processing/
│
├── main.py               # Main entry point for the program
├── process_manager.py    # Module for managing processes
├── thread_manager.py     # Module for managing threads
├── file_processing.py    # Module for parallel text file processing
└── utils.py              # Utility functions and shared functionalities

-main.py: Contains the main program logic and CLI user interface.

-process_manager.py: Handles process-related functionalities such as listing, killing, suspending, and resuming processes.

-thread_manager.py: Handles thread-related functionalities such as listing and killing threads.

-file_processing.py: Implements functions for parallel text file processing, including loading and distributing file segments, processing segments in parallel, and combining results.

-utils.py: Contains utility functions and shared functionalities used across modules.

## Instructions:

-Clone or download the project repository.
-Ensure Python is installed on your system.
-Install the required dependencies by running pip install -r requirements.txt.
-Run the program by executing python main.py.
-Follow the prompts in the CLI menu to interact with the task manager and perform text file processing.

## Output Screenshots:

![OUTPUT 1](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/8683e2c4-ec62-4a3e-a397-539570709987)

## Discussion of findings, challenges, limitations, and areas for improvement:

### Findings:

The project successfully implements a multi-process and multi-thread task manager with additional text file processing functionalities. It also demonstrates the capabilities of multiprocessing and multithreading in Python for system management and parallel processing tasks. With further refinement and optimization, it could be a valuable tool for system administrators and developers. The CLI interface provides a user-friendly way to interact with the program.
### Challenges:

Permissions based on local machine was an early issue (that is still persisting in some cases). Also, ensuring proper synchronization and communication between processes/threads was a challenge.
### Limitations:

The current implementation may not be optimal for extremely large text files or systems with limited resources. Error handling and edge cases could also be further improved for robustness.
### Areas for improvement:

Some areas for imporovement are to firstly ensure all cases and functions are operational and do not break the program based on permisssion issues. Error handling to provide more informative error messages to users. Options for customizing parallelization parameters based on system resources is also an addition that can be added in the future.
