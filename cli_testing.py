import json

class MemoryManager:
    def __init__(self):
        self.allocated_memory = {}  # Dictionary to store allocated memory blocks

    def alloc(self, process):
        # Implement your BestFit memory allocation algorithm here
        # This example assumes a simple BestFit logic for demonstration purposes.
        # You'll need to replace this with the actual BestFit algorithm
        if not process:
            return

        # Find a suitable memory block using the BestFit algorithm
        best_block_size = float('inf')  # Initialize with a large value
        best_block_address = None
        for address, size in self.allocated_memory.items():
            if size >= process.memory_requirement and size < best_block_size:
                best_block_size = size
                best_block_address = address

        if best_block_address is not None:
            self.allocated_memory[best_block_address] = process
            print(f"Process {process.name} allocated to memory block {best_block_address}")
        else:
            print(f"Insufficient memory to allocate process {process.name}")

    def show(self):
        return self.allocated_memory

class Process:
    def __init__(self, name, owner, memory_requirement):
        self.name = name
        self.owner = owner
        self.memory_requirement = memory_requirement

class ProcessManager:
    def __init__(self):
        self.processes = {}  # Dictionary to store created processes

    def create(self, filename, owner, memory_requirement):
        process = Process(filename, owner, memory_requirement)
        self.processes[process.name] = process
        return process

    def get(self, process_name):
        return self.processes.get(process_name)

    def show(self):
        return self.processes

if __name__ == "__main__":
    memory_m = MemoryManager()
    process_m = ProcessManager()

    p1 = process_m.create("a.cpp", "allex", 10)  # Assuming memory requirements are specified
    p2 = process_m.create("b.py", "daniel", 20)
    p3 = process_m.create("c.js", "paulo", 30)
    p4 = process_m.create("d.lua", "renan", 15)

    print("\nProcessos:")
    for process in process_m.show().values():
        print(f"{process.name} ({process.owner}) - {process.memory_requirement} MB")

    # print("\nEspaços de Memória: ", json.dumps(memory_m.show(), indent=4))

    memory_m.alloc(p1)
    memory_m.alloc(p2)
    memory_m.alloc(p3)
    memory_m.alloc(p4)

    print("\nAlocações com o BestFit:")
    print(json.dumps(memory_m.show(), indent=4))
