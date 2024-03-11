import os
import multiprocessing
import time
from collections import Counter

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
def process_large_text_file():
    filename = input("Enter the path to the large text file: ")
    num_segments = int(input("Enter the number of segments to split the file into: "))
    num_processes = int(input("Enter the number of processes to use: "))

    start_time = time.time()
    result = process_parallel(filename, num_segments, num_processes)
    end_time = time.time()

    print("Results:")
    print(result)
    print("Time taken: {} seconds".format(end_time - start_time))
