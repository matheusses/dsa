class Stack:

    def __init__(self):
        self.items = [0]
        self.last_pos = -1

    def push(self, item):
        if self.last_pos == len(self.items)-1:
            self.items += len(self.items)*[0]
        self.last_pos += 1
        self.items[self.last_pos] = item 

    def pop(self):
        if not self.is_empty():
            last_item = self.items[self.last_pos]
            self.items[self.last_pos] = None
            self.last_pos -= 1
            return last_item

    def peek(self):
        if not self.is_empty():
            return self.items[self.last_pos]

    def is_empty(self):
        return self.last_pos < 0

# using stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.pop())  
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
# 1