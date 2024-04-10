import datetime
import random  # Assuming random values are used for process attributes

class Process:
    def __init__(self, name, user):
        self.pid = None
        self.name = name
        self.context = {}  # Context dictionary for process registers
        self.user = user
        self.priority = None
        self.size = None
        self.start_time = None
        self.state = None
        self.__generate_attributes()

    def __generate_attributes(self):
        """
        Generates pseudo-random values for process attributes.
        """

        self.pid = random.randint(1, 10000)  # Random PID

        # Assuming priority range is -20 to 19 (needs clarification)
        self.priority = random.randint(-20, 19)

        # Process size in KiB (assuming KiB is the desired unit)
        self.size = random.randint(1, 1024)  # Random size

        # Context with random register values (needs clarification on register names)
        for _ in range(random.randint(2, 10)):
            self.context.update({f"register_{random.randint(1, 32)}": hex(random.randint(0, 16**8))})

        self.start_time = datetime.datetime.now().isoformat()
        self.state = "waiting"  # Default state


class ProcessManager:
    def __init__(self):
        self.processes = []

    @staticmethod
    def __process_listing_style(obj):
        """
        Defines the format for process information display.
        """
        return {
            'pid': obj.pid,
            'name': obj.name,
            'user': obj.user,
            'priority': obj.priority,
            'state': obj.state,
            'size': f"{obj.size} KiB",
            'start_time': obj.start_time,
            'context': obj.context,
        } if not hasattr(ProcessManager, 'TESTING') or not ProcessManager.TESTING else {
            'pid': obj.pid,
            'size': f"{obj.size} KiB",
        }

    def create(self, name, user):
        """
        Creates a new process object and adds it to the process list.
        """
        process = Process(name, user)
        self.processes.append(process)
        return process.pid

    def get(self, pid):
        """
        Returns the process object with the given PID.
        """
        for process in self.processes:
            if process.pid == pid:
                return process
        return None

    def show(self, pid=None):
        """
        Returns information about a specific process or all processes.
        """
        if pid:
            process = self.get(pid)
            if process:
                return ProcessManager.__process_listing_style(process)
            else:
                return None
        else:
            return [ProcessManager.__process_listing_style(process) for process in self.processes]

    def kill(self, pid):
        """
        Removes the process object with the given PID from the list.
        """
        self.processes = [process for process in self.processes if process.pid != pid]


