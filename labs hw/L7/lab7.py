# lab 7
#q1

def sortlst(lst):
    for i in range(len(lst)-1):
        if lst[i] != i+1:
            lst[i], lst[lst[i]] = lst[lst[i]], lst[i]
    return lst

# lst = [2,0,1,3]
# sortlst(lst)
# print(lst)

def intersectionOfLst(lst1,lst2):
    p1, p2 = 0,0
    start_ind, end_ind = None,None 
    while p1 < len(lst1) and p2 < len(lst2):
        if p1==p2 and start_ind == None:
            start_ind = lst1.index(lst2[p2])
        elif p1==p2 and start_ind != None:
            end_ind = lst1.index(lst2[p2])
        elif p1>p2:
            p2+=1
        elif p2>p1:
            p1+=1
    return lst1[start_ind:end_ind+1]

lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
print(intersectionOfLst(lst1,lst2))

def ispoweroftwo(n):
    if n == 1:
        return False
    if n == 0:
        return True
    else:
        return ispoweroftwo(n//2)
    
# print(ispoweroftwo(13))
# print(ispoweroftwo(35))
# print(ispoweroftwo(18))


def split_parity(lst, low, high):
    if lst[low] % 2 == 0:
        low += 1
    elif lst[high] % 2 != 0:
        high -= 1
    else:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    return split_parity(lst, low, high) if low < high else lst


# lst = [4, -5, 2, 3, -1, -6, 7, 9, 0]
# split_parity(lst, 0, len(lst) - 1)
# print(lst)


def nested_sum(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total

# print(nested_sum([[1,2],3,[4,[5,6,[7],8]]]))