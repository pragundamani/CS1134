#q5 answer pd2752
#q5 answer pd2752

from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

def permutations(lst):
    permstack = ArrayStack()
    permqueue = ArrayQueue()

    for i in lst:
        permstack.push(i)

    permqueue.enqueue([])

    while not permstack.is_empty():
        size = len(permqueue)
        current = permstack.pop()

        for j in range(size):
            temp = permqueue.dequeue()
            for k in range(len(temp) + 1):
                new_perm = temp[:k] + [current] + temp[k:]
                permqueue.enqueue(new_perm)
    
    res = []
    while not permqueue.is_empty():
        res.append(permqueue.dequeue())
    
    return res
