# COMPSC472Proj1
Repo for Project 1 of COMPSC 472

## Description of the project:

The project aims to create a multi-process and multi-thread task manager with additional features for parallel text file processing. It provides functionalities to manage processes and threads, including listing processes/threads, killing processes/threads, suspending/resuming processes, and more. Additionally, it allows users to process large text files efficiently using parallelization techniques, such as multiprocessing.

## Structure with diagram and descriptions:

![image](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/9793e38a-8e7b-4e22-b200-24c9b6b3d7d5)

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
![OUTPUT 2-4](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/390c9285-c46b-4d75-b1c3-8be3ad53a2ad)
![OUTPUT 5](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/09d198ef-7597-4f5f-a17d-11fe90257674)
![OUTPUT 6-8](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/2a2ff281-a599-4c77-ab95-cc2ec025540e)
![OUTPUT 9-10](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/a9aae612-1108-4968-a9f9-09b0e76e1b8b)
![OUTPUT 11](https://github.com/MajaSLash/COMPSC472Proj1/assets/52076286/5f0e83ca-7427-442a-bda9-ea436b6ea30d)





## Discussion of findings, challenges, limitations, and areas for improvement:

### Findings:

The project successfully implements a multi-process and multi-thread task manager with additional text file processing functionalities. It also demonstrates the capabilities of multiprocessing and multithreading in Python for system management and parallel processing tasks. With further refinement and optimization, it could be a valuable tool for system administrators and developers. The CLI interface provides a user-friendly way to interact with the program.
### Challenges:

Permissions based on local machine was an early issue (that is still persisting in some cases). Also, ensuring proper synchronization and communication between processes/threads was a challenge.
### Limitations:

The current implementation may not be optimal for extremely large text files or systems with limited resources. Error handling and edge cases could also be further improved for robustness.
### Areas for improvement:

Some areas for imporovement are to firstly ensure all cases and functions are operational and do not break the program based on permisssion issues. Error handling to provide more informative error messages to users. Options for customizing parallelization parameters based on system resources is also an addition that can be added in the future.
