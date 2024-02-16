class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
        self.max_size = 3

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.items.append(item)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.items.pop()
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[self.top]

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:")
            for item in reversed(self.items):
                print(item)

s = Stack()
s.push(5)
s.push(7)
s.push(9)  # This should work fine.
s.push(11) # This should raise an IndexError as the stack is full.
