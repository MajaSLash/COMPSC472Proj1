import os
import psutil
import signal

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