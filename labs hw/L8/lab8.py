# lab 8
from ArrayStack import ArrayStack

def stack_sum(stack):
    if stack.is_empty():
        return 0
    total = stack.pop() + stack_sum(stack)
    stack.push(total)
    return total
    
    
stck = ArrayStack()
for i in range(5):
    print(i + 1)
    stck.push(i + 1)
print(stack_sum(stck))
# for i in range(len(stck)):
    # print(stck.pop())



def flatten_list(lst):
    stack = ArrayStack() # make stacks for data
    for item in lst: # go thrugh lst
        while isinstance(item, list): #check is list or nested 
            for subitem in item:  # denest list
                stack.push(subitem)  # add to stack
            item = stack.pop() # next thing in list 
        stack.push(item)   # add to main stack
    
    while len(lst) > 0:  
        lst.pop()  # clearance
    
    while len(stack) > 0:  
        lst.insert(0, stack.pop())  # put back in list in order
        

# lst = [[1, 2, [3]], 4, [5, 6]]
# flatten_list(lst)
# print(lst)

def stack_sorter(s):
    helper = ArrayStack()
    while len(s) > 0:
        temp = s.pop()
        
        while len(helper) > 0 and helper.top() > temp:
            s.push(helper.pop())
        helper.push(temp)
        
    while len(helper) > 0:
        s.push(helper.pop())    
        
# stck = ArrayStack()
# for i in [3, 1, 4, 2]:
#     stck.push(i)
# stack_sorter(stck)
# while len(stck) > 0:
#     print(stck.pop()) 