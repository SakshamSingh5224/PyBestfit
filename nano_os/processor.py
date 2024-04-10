import datetime
import random


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
        You can adjust the ranges for priority and size based on your needs.
        """

        self.pid = random.randint(1, 10000)  # Random PID

        # Assuming priority range is -20 (low) to 19 (high)
        self.priority = random.randrange(-20, 20)

        # Process size in KiB (assuming KiB is the desired unit)
        self.size = random.randint(1, 1024)  # Random size

        # Context with random register values (replace with actual register names)
        for _ in range(random.randint(2, 10)):
            register_name = f"reg_{random.randint(1, 32)}"
            register_value = hex(random.randint(0, 16**8))
            self.context.update({register_name: register_value})

        self.start_time = datetime.datetime.now().isoformat()
        self.state = "waiting"  # Default state


class ProcessManager:
    def __init__(self):
        self.processes = []
        self.TESTING = False  # Set to True for potential testing modifications

    def __process_listing_style(self, obj):
        """
        Defines the format for process information display.
        """
        output_data = {
            "pid": obj.pid,
            "name": obj.name,
            "user": obj.user,
            "priority": obj.priority,
            "state": obj.state,
            "size": f"{obj.size} KiB",
            "start_time": obj.start_time,
            "context": obj.context,
        }
        if self.TESTING:
            # Potential modifications for testing (example: exclude context)
            del output_data["context"]
        return output_data

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
                return self.__process_listing_style(process)
            else:
                return None
        else:
            return [self.__process_listing_style(process) for process in self.processes]

    def kill(self, pid):
        """
        Removes the process object with the given PID from the list.
        Raises an exception if the process is not found.
        """
        try:
            self.processes.remove([process for process in self.processes if process.pid == pid][0])
        except IndexError:
            raise ProcessNotFoundException(f"Process with PID {pid} not found")

class ProcessNotFoundException(Exception):
    """
    Custom exception raised when a process with a given PID is not found.
    """
    pass


# Example usage
if __name__ == "__main__":
    process_manager = ProcessManager()

    # Create some processes
    process_manager.create("Process 1", "user1")
    process_manager.create("Process 2", "user2")
    process_manager.create("Process 3", "user3")

    # Show information about all processes
    print("All processes:")
    print(process_manager.show())

    # Show information about a specific process
    process_info = process_manager.show(2)



