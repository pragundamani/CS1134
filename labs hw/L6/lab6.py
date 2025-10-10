# lab 6
def sum_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to(n - 1)

# print(sum_to(5))

def product_evens(n):
    if n <= 0:
        return 1
    else:
        if n%2 == 0:
            return n*product_evens(n-2)
        else:
            return product_evens(n-1)

# print(product_evens(8))

# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     prev  = find_max(lst[1:]) 
#     '''runtime is O(n^2) since slicing happens 
#         n times and takes n duration''' 
#     if prev > lst[0]:
#         return prev
#     return lst[0]

# print(find_max([1,2,3,4,5]))
# print(find_max( [13, 9, 16, 3, 4, 2]))

def find_max(lst, low, high, max=None):
    if max is None:
        max = lst[low]
    if low > high:
        return max
    if lst[low] > max:
        max = lst[low]
    return find_max(lst, low + 1, high, max)

# print(find_max([13, 9, 16, 3, 4, 2], 3, 5))

def is_palindrome(str, low, high):
    if low >= high:
        return True
    if str[low] != str[high]:
        return False
    return is_palindrome(str, low+1, high-1)

# print(is_palindrome("abba", 0, 3))
# print(is_palindrome("abcba", 0, 4))
# print(is_palindrome("abca", 0, 3))
# print(is_palindrome("abcd", 0, 3))

def binary_search(lst, low,high, val):
    if low >= high:
        return False
    mid = (low + high)//2
    if lst[mid] == val:
        return True
    elif lst[mid] > val:
        return binary_search(lst, low, mid, val)
    else:
        return binary_search(lst, mid+1, high, val)