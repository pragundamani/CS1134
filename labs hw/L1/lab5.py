##### Q2 #####
def find_pivot(lst):
    if not lst:
        return None
    
    left = 0
    right = len(lst) - 1
    
    if lst[left] <= lst[right]:
        return left
    
    while left < right:
        mid = (left + right) // 2

        if lst[mid] > lst[right]:
            left = mid + 1

        else:
            right = mid
    
    return left


def shift_binary_search(lst, target):
    if not lst:
        return None
    
    pivot = find_pivot(lst)
    
    if pivot is None:
        return None
    
    n = len(lst)
    
    if pivot == 0:
        return binary_search(lst, target, 0, n - 1)

    if target >= lst[0]:
        return binary_search(lst, target, 0, pivot - 1)
    else:
        return binary_search(lst, target, pivot, n - 1)


def binary_search(lst, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None


