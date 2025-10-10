def split_parity(lst):
    # odds = [i for i in lst if i%2 != 0]
    # evens = [j for j in lst if j%2 == 0]
    # # print(odds)
    # # print(evens)
    # return odds+evens
    left = 0  
    right = len(lst) - 1 
    
    while left < right:
        while left < right and lst[left] % 2 == 1:
            left += 1
        
        while left < right and lst[right] % 2 == 0:
            right -= 1
        
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    return lst


print(split_parity([1,2,3,4,5,6,7,8,9]))