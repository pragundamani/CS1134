#q4 answer pd2752
def list_min(lst,low,high):
    if low==high:
        return lst[low]
    else:
        mid = (low+high)//2
        left_min = list_min(lst,low,mid)
        right_min = list_min(lst,mid+1,high)
        return left_min if left_min < right_min else right_min
    
# print(list_min([3,1,4,1,5,9,2,6,5,3,5],4,10))