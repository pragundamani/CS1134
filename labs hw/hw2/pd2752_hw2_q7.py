#q7 answer pd2752
def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    while left < right:
        mid = (left + right) // 2
        if lst01[mid] == 0:
            left = mid + 1
        else:
            right = mid
    if lst01[left] == 1:
        return left
    else:
        return float('-inf')

# print(findChange([0,0,0,1,1,1])) 
# print(findChange([0,0,0,0]))      