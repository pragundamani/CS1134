#q2 answer pd2752
from ArrayStack import ArrayStack

class MaxStack():
    
    def __init__(self):
        self.stack = ArrayStack()
        self.max = None
    
    def push(self, item):
        if self.max != None and item > self.max:
            self.max = item
            self.stack.push(item)
        elif self.max == None:
            self.max = item
            self.stack.push(item)
        else:
            self.stack.push(item)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.stack.pop()
        if item == self.max:
            self.max = None
            temp_stack = ArrayStack()
            while not self.stack.is_empty():
                temp_item = self.stack.pop()
                if self.max == None or temp_item > self.max:
                    self.max = temp_item
                temp_stack.push(temp_item)
            while not temp_stack.is_empty():
                self.stack.push(temp_stack.pop())
        return item
    
    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.max
    
    def is_empty(self):
        return self.stack.is_empty()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.top()

    def __len__(self):
        return len(self.stack)

