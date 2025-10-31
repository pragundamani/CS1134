# lab 9
from ArrayQueue import *
    
class MeanQueue():
    def __init__(self):
        self.data = ArrayQueue()
        self.total_sum = 0
        self.front_ind = 0 
        self.n = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, elem):
        self.data.enqueue(elem)
        self.total_sum += elem

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data.dequeue()
        self.total_sum -= value
        return value

    def mean(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.total_sum / len(self.data)

def test_mean_queue():
    q = MeanQueue()
    for i in range(1, 6):
        q.enqueue(i)
        print(f"Mean after enqueuing {i}:", q.mean())
    for i in range(1, 6):
        q.dequeue()
        if not q.is_empty():
            print(f"Mean after dequeuing {i}:", q.mean())

#print("Testing MeanQueue:")
#test_mean_queue()

class ArrayDeque():
    def __init__(self):
        self.data = [None] * 4
        self.front = 0
        self.n = 0
    def __len__(self): 
        return self.n
    def is_empty(self):
        return self.n == 0
    
    def first(self):
        if self.n == 0:
            raise Exception("Queue is empty")
        else:
            return self.data[self.front]
    def last(self):
        if self.n == 0:
            raise Exception("Queue is empty")
        else:
            back = (self.front + self.n - 1) % len(self.data)
            return self.data[back]

    def enqueue_first(self, elem):
        if self.n == len(self.data):
            for i in range(len(self.data)//2):
                self.data.append(None)
            self.front= (self.front - len(self.data)) % len(self.data)
        else:
            self.front = (self.front - 1) % len(self.data)
            self.data[self.front] = elem
            self.n += 1
    def enqueue_last(self, elem):
        if self.n == len(self.data)-1:
            self.data.append(elem)
        else:
            back = (self.front + self.n) % len(self.data)
            self.data[back] = elem
            self.n += 1
    
    def dequeue_first(self):
        if self.n == 0:
            raise Exception("Queue is empty")
        else:
            res = self.front
            self.data[self.front] = None
            self.front = (self.front + 1) % len(self.data)
            self.n -= 1
            return res
    def dequeue_last(self):
        if self.n == 0:
            raise Exception("Queue is empty")
        else:
            self.n -= 1
            return self.data.pop()


def test_array_deque():
    d = ArrayDeque()
    d.enqueue_last(1)
    d.enqueue_last(2)
    d.enqueue_last(3)
    print("Deque after enqueuing last 1, 2, 3:", [d.data[i] for i in range(len(d.data))])
    d.enqueue_first(0)
    print("Deque after enqueuing first 0:", [d.data[i] for i in range(len(d.data))])
    print("First element:", d.first())
    print("Dequeue first:", d.dequeue_first())
    print("Deque after dequeuing first:", [d.data[i] for i in range(len(d.data))])
    print("Dequeue last:", d.dequeue_last())
    print("Deque after dequeuing last:", [d.data[i] for i in range(len(d.data))])

print("Testing ArrayDeque:")
test_array_deque()
