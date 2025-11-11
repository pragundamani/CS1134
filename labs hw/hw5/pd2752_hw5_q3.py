#q3 answer pd2752
from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack

class MidStack:

    def __init__(self):
        self.front = ArrayStack()
        self.back = ArrayDeque()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.front)+len(self.back)

    def push(self, item):
        self.back.enqueue_last(item)
        if len(self.back) > len(self.front) +1:
            self.front.push(self.back.dequeue_first())

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if len(self.back) >= len(self.front):
            item = self.back.dequeue_last()
        else:
            item = self.front.pop()
        if len(self.back) < len(self.front):
            self.back.enqueue_first(self.front.pop())
        return item

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if len(self.back) > 0:
            return self.back.last()
        else:
            return self.front.top()

    def mid_push(self, item):
        if len(self.back) > len(self.front):
            self.front.push(self.back.dequeue_first())
        else:
            self.back.enqueue_first(item)
    
