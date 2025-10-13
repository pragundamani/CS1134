# q3 answer pd2752
def find_duplicates(lst):
    size = len(lst)
    duplicates = [0]*size
    for num in lst:
        duplicates[num]+=1
    result = []
    for i in range(1,size):
        if duplicates[i]>1:
            result.append(i)
    return result

# lst = [2,4,4,1,2]
# print(find_duplicates(lst))