from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()

    for x in lst:
        stack.push(x)

    queue.enqueue([])

    while not stack.is_empty():
        x = stack.pop()
        curr_level_size = len(queue)

        for _ in range(curr_level_size):
            perm = queue.dequeue()
            m = len(perm)

            for i in range(m + 1):
                new_perm = perm.copy()
                new_perm.insert(i, x)
                queue.enqueue(new_perm)

    result = []
    while not queue.is_empty():
        result.append(queue.dequeue())

    return result