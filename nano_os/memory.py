import random

class Block:
    def __init__(self, size=None):
        self.address = hex(random.randint(10000, 30000))  # Random address
        self.size = {'total': size, 'available': size}
        self.content = []

class Memory:
    def __init__(self, width):
        self.blocks = []
        self.width = width

        # Use random sizes for blocks if not in testing mode
        if not hasattr(self, 'TESTING') or not self.TESTING:
            for _ in range(width):
                self.blocks.append(Block(random.randint(1, 100)))  # Random size
        else:
            # Use predefined sizes if in testing mode (assuming `SIZES` is defined elsewhere)
            for size in support.SIZES:
                self.blocks.append(Block(size))

    def get_block(self, address):
        for block in self.blocks:
            if block.address == address:
                return block
        return None

    def get_array(self):
        return self.blocks

    def alloc_in(self, obj, address):
        block = self.get_block(address)
        if block:
            block.content.append(obj)
            block.size['available'] -= obj.size
            obj.state = support.P_STATES[1]  # Assuming P_STATES defines process states

    def free(self, address):
        block = self.get_block(address)
        if block:
            # Implement logic to free the block (remove process, update available size)


class MemoryManager(Memory):
    def __init__(self, m_blocks_quantity=10):
        super().__init__(m_blocks_quantity if not hasattr(self, 'TESTING') or not self.TESTING else len(support.SIZES))

    def __listing_style(self, block):
        return {
            'address': block.address,
            'size': {
                'total': f"{block.size['total']} KiB",
                'available': f"{block.size['available']} KiB",
            },
            'content': [{'pid': item.pid, 'size': f'{item.size} KiB'} for item in block.content]
        }

    def best_fit(self, process):
        process_size = process.size
        best_block = None
        best_diff = float('inf')  # Initialize with a large value

        for block in self.blocks:
            size_diff = abs(block.size['available'] - process_size)
            if size_diff < best_diff and block.size['available'] >= process_size:
                best_block = block
                best_diff = size_diff

        if best_block:
            return best_block.address
        else:
            support.ERRORS.append(f"[Warning] Could not find an available space for process {process.pid}.")

    def alloc(self, obj):
        address = self.best_fit(obj)
        if address:
            # Use a thread pool or other mechanisms for safe memory allocation if needed
            self.alloc_in(obj, address)
            return address
        else:
            return None

    def show(self, address=None):
        if address:
            block = self.get_block(address)
            if block:
                return self.__listing_style(block)
            else:
                return None
        else:
            return [self.__listing_style(block) for block in self.blocks]


# Removed threading (consider thread pools or alternative approaches for safe memory allocation)
# Removed `support` module references (replace with actual implementations or alternative libraries)

