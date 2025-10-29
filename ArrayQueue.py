from ArrayList import *

class StaticArrayQueue:
    def __init__(self, max_capacity):
        self.data_arr = make_array(max_capacity) 
        self.capacity = max_capacity
        self.n = 0
        self.front_ind = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return len(self) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        
        if self.is_empty():
            self.data_arr[self.front_ind] = item
        
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = item
            self.n += 1
        

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        value = self.data_arr[self.front_ind] 
        self.data_arr[self.front_ind] = 0
        self.front = (self.front + 1) % self.capacity
        self.n -= 1
        
        if self.n == 0:
            self.front_ind = 0

        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]


class ArrayQueue:
    def __init__(self):
        self.data_arr = ArrayList()














