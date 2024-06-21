class BitArray:
    def __init__(self, size: int):
        self.size = size
        self.array = 0

    def set(self, i, val):

        if val not in (0, 1):
            raise ValueError("Value must be either 0 or 1")
        
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        
        if val == 1:
            self.array |= (1 << i)
        else:
            self.array &= ~(1 << i)
    
    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return (self.array >> i) & 1

bit_array = BitArray(10)  # Initialize bit array of size 10
bit_array.set(3, 1)       # Set index 3 to 1
print(bit_array.get(3))   # Should output 1
bit_array.set(3, 0)       # Set index 3 to 0
print(bit_array.get(3))   # Should output 0