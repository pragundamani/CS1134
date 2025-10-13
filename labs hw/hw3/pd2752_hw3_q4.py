#q4 answer pd2752
def remove_all(lst, value):
    ind = 0
    for i in range(len(lst)):
        if lst[i] != value:
            lst[ind] = lst[i]
            ind += 1
    for j in range(len(lst) - ind):
        lst.pop()