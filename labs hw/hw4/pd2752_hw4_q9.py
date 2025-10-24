def permutations(lst,low,high):
    sub = lst[low:high+1]
    if len(sub)==0:
        return []
    if len(sub)==1:
        return [[sub[0]]]
    out = []
    for i in range(len(sub)):
        elem = sub[i]
        rem = sub[:i]+ sub[i+1:]
        for p in permutations(rem,0,len(rem)-1):
            out.append([elem]+p)
    return out

# lst = [1,2,3]
# print(permutations(lst,0,2))