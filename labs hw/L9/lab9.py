# lab 9
from ArrayQueue import ArrayQueue
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
