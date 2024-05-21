class MultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * (stack_size * 3)
    
    def _calculate_top_index(self, stack_number):
        offset = stack_number * self.stack_size
        for i in range(self.stack_size):
            if self.list[offset + i] is None:
                return offset + i - 1
        return offset + self.stack_size - 1
    
    def pop(self, stack_number):
        top_index = self._calculate_top_index(stack_number)
        
        if top_index < stack_number * self.stack_size:
            raise IndexError("pop from empty stack")
        
        item = self.list[top_index]
        self.list[top_index] = None
        return item
    
    def push(self, item, stack_number):
        top_index = self._calculate_top_index(stack_number)
        if top_index >= (stack_number + 1) * self.stack_size - 1:
            raise IndexError("push to full stack")
        self.list[top_index + 1] = item

s = MultiStack(5)
s.push(1, 0)
s.push(2, 0)
s.push(3, 1)
s.push(4, 2)

print(s.pop(0))  # Output: 2
print(s.pop(1))  # Output: 3
print(s.pop(2))  # Output: 4
print(s.pop(0))  # Output: 1
        
       