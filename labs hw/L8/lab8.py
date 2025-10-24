# lab 8
from ArrayStack import ArrayStack

def stack_sum(stack):
    total = 0
    for i in range(len(stack)):
        total += stack.pop()
    return total

# stck = ArrayStack()
# for i in range(5):
    # print(i + 1)
    # stck.push(i + 1)
# print(stack_sum(stck))



def flatten_list(lst):
    pass

lst = [[1, 2, [3]], 4, [5, 6]]
flatten_list(lst)
print(lst)

def stack_sorter(s):
    min = float("inf")
    helper = ArrayStack()
    while not s.isempty():
        if s.top() < min:
            min = s.top()
        temp = s.pop()
        while not helper.isempty() and helper.top() > temp:
            s.push(helper.pop())
        helper.push(temp)
    while not helper.isempty():
        s.push(helper.pop())
        
        
stck = ArrayStack()
for i in [3, 1, 4, 2]:
    stck.push(i)
stack_sorter(stck)
print(stack_sorter(stck))