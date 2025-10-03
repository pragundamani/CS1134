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

nums = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]

print("=== Testing Rotated Sorted Array Search ===")
print(f"Array: {nums}")


pivot_index = find_pivot(nums)
print(f"\nPart A - Pivot index: {pivot_index}")
print(f"Minimum value at pivot: {nums[pivot_index] if pivot_index is not None else 'None'}")

target = 21
result = shift_binary_search(nums, target)
print(f"\nPart B - Searching for {target}: index {result}")

test_cases = [1, 3, 6, 7, 10, 12, 14, 15, 20, 21, 99]
print(f"\nTesting all values:")
for val in test_cases:
    idx = shift_binary_search(nums, val)
    print(f"  {val}: {'Found at index ' + str(idx) if idx is not None else 'Not found'}")

sorted_array = [1, 3, 6, 7, 10, 12, 14, 15, 20, 21]
print(f"\nTesting with non-rotated array: {sorted_array}")

pivot = find_pivot(sorted_array)
print(f"Pivot: {pivot}")

target_idx = shift_binary_search(sorted_array, 21)
print(f"Search for 21: index {target_idx}")