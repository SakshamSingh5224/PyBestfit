# Imports
from processor import ProcessManager
from memory import MemoryManager

# Optional: Consider using argparse for command-line arguments
# import argparse

# Author and License Information (Optional: Move to separate file)
__author__ = "Allex Lima"
__copyright__ = "Copyright (c) 2016 Allex Lima"
__credits__ = ["Allex Lima", "Daniel Bispo", "Paulo Moraes", "Renan Barroncas"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Allex Lima"
__email__ = "allexlima@unn.edu.br"
__status__ = "Production"


def main():
    """
    Main function for process and memory management.
    """

    # Create process and memory managers
    process_manager = ProcessManager()
    memory_manager = MemoryManager(total_memory=1024)  # Set total available memory

    # Example process creation (replace with your actual logic)
    processes = [
        process_manager.create_process("Process 1", 100),
        process_manager.create_process("Process 2", 200),
        process_manager.create_process("Process 3", 300),
    ]

    # Allocate memory for processes (handle potential allocation failures)
    for process in processes:
        if not memory_manager.allocate_memory(process):
            print(f"Insufficient memory to allocate for process {process['name']}")
            continue  # Skip to next process if allocation fails

    # Simulate process execution (replace with your logic)
    for process in processes:
        print(f"Process {process['name']} is running...")
        # Simulate some processing time
        import time
        time.sleep(2)

    # Deallocate memory for finished processes
    for process in processes:
        memory_manager.deallocate_memory(process)
        process_manager.finish_process(process)

    print("All processes finished. Memory deallocated.")


if __name__ == "__main__":
    main()


