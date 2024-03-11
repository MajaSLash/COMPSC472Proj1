import os
import psutil
import signal

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