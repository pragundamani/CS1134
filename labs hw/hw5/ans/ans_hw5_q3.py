from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack

class MidStack:
    def __init__(self) -> None:
        self.left = ArrayStack()
        self.right = ArrayDeque()

    def __len__(self):
        return len(self.left) + len(self.right)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, val):
        self.right.enqueue_last(val)

        if len(self.right) > len(self.left):
            self.left.push(self.right.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        
        if len(self.right) == 0:
            return self.left.top()
        return self.right.last()
    
    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        
        if len(self.right) == 0:
            return self.left.pop()

        res = self.right.dequeue_last()

        if len(self.left)-1 > len(self.right):
            self.right.enqueue_first(self.left.pop())

        return res
    
    def mid_push(self, val):
        self.left.push(val)

        if len(self.left)-1 > len(self.right):
            self.right.enqueue_first(self.left.pop())