#q6 answer pd2752
def two_sum(srt_lst,target):
    left = 0
    right = len(srt_lst)-1
    while left<right:
        sum = srt_lst[left]+srt_lst[right]
        if sum == target:
            return (left,right)
        elif sum < target:
            left+= 1
        else:
            right-= 1
    return None

# print(two_sum([-2, 7, 11, 15, 20, 21],22))