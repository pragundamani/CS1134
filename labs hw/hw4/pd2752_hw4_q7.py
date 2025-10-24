#q7 answer pd2752
def split_by_sign(lst,low,high):
    if low>high:
        return low
    if lst[low]<0:
        return split_by_sign(lst,low+1,high)
    if lst[high]>=0:
        return split_by_sign(lst,low,high-1)
    lst[low],lst[high] = lst[high],lst[low]
    return split_by_sign(lst,low+1,high-1)
        
# lst = [4,-3,2,-1,0,-5,6]
# split_by_sign(lst,0,len(lst)-1)
# print(lst)

