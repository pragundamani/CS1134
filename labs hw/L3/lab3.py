'''
Q1
a
'''
def reverse_list(lst):
    low, high = 0, len(lst) - 1
    while low < high:
        lst[low], lst[high] = lst[high], lst[low] 
        low += 1
        high -= 1

lst = [1, 2, 3, 4, 5, 6]
reverse_list(lst)

'''
b
'''
def reverse_list(lst, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    while low < high:
        lst[low], lst[high] = lst[high], lst[low] 
        low += 1
        high -= 1

'''
Q2
'''
def power_of_2(n):
    value = 1
    for i in range(n):
        yield value
        value *= 2

'''
Q3
'''
def move_zeroes(nums):
    pointer = 0
    for i in range(0,len(nums)-1):
        if nums[i]!=0 and i != pointer:
            nums[i], nums[pointer] = nums[pointer],nums[i]
            pointer+=1
    
nums=[0, 1, 0, 3, 13, 0]
#move_zeroes(nums)
#print(nums)

'''
Q4
'''
def shifter(nums,shifts):
    for i in range(len(nums)-shifts):
        nums[i], nums[i+shifts] = nums[i+shifts], nums[i]

#shifter(nums,2)
#print(nums)