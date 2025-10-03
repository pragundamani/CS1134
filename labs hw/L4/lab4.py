'''Q1'''
def is_palindrome(s):
    lst = list(s)
    left, right = 0,len(lst)-1
    while left<right:                        # simple binary search compares back of list to front and reduces both valeus, if they are different
        if lst[left]!=lst[right]:            # loop breaks else continues
            return False
        else:
            left+=1
            right-=1
        #print(left,right)
    return True

# print(is_palindrome("hello"))
# print(is_palindrome("ororo"))
# print(is_palindrome("abba"))

'''Q2'''
def reverse_vowels(input_str):
    list_str = list(input_str)
    left,right =  0,len(list_str)-1,
    while left<right:
        if list_str[left] in "aeiou" and list_str[right] not in "aeiou":
            right -= 1
        elif list_str[right] in "aeiou" and list_str[left] not in "aeiou":
            left += 1
        elif list_str[left] in "aeiou" and list_str[right] in "aeiou":
            list_str[left], list_str[right] = list_str[right], list_str[left]
            left+= 1
            right-= 1
        else:
            left+= 1
            right-= 1


    return "".join(list_str)

# print(reverse_vowels("tandon"))
# print(reverse_vowels("mousse"))

'''Q3'''
def maxsum(nums,k):
    slider = [0,k-1]
    size = len(nums)-1
    max = nums[0]
    while slider[1]<=size:
        temp = sum(nums[slider[0]:slider[1]+1])
        if max<temp:
            max = temp
        else:
            slider[0] += 1
            slider[1] += 1
    if max == -9999999999:
        return "window larger than list"
    return max

print(maxsum([1,12,-5,-6,50,3,9],3))

'''Q4'''
#a n^2

def sorted_find_missing(lst):
    if lst[0]!=0:
        return 0
    

def usorted_find_missing(lst):
    total = 0
    for i in range(0,len(lst)+1):
        total += i
        # print(total,i)
    return total-sum(lst)

# print(usorted_find_missing([0, 1, 2, 3, 4, 5, 6, 8]))

def sorted_find_missing(lst):
    left, right = 0, len(lst)-1
    while left<right:
        mid = (left+right)//2
        #print(mid)
        if mid == lst[mid]:
            left = mid + 1
        else:
            right = mid -1
    return left

    
#print(sorted_find_missing([0, 1, 2, 3, 4, 5, 6, 8]))