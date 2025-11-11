#q4 answer pd2752
from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.queuestack = ArrayStack()
        self.helpstack = ArrayStack()

    def __len__(self):
        return len(self.queuestack) + len(self.helpstack)
   
    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.queuestack.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.helpstack.is_empty():
            while not self.queuestack.is_empty():
                self.helpstack.push(self.queuestack.pop())
        return self.helpstack.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.helpstack.is_empty():
            while not self.queuestack.is_empty():
                self.helpstack.push(self.queuestack.pop())
        return self.helpstack.top()
