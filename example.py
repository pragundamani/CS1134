<<<<<<< HEAD
def find(root,key):
    if root is None:
        return ['fail']
    elif root.value == key:
        return []
    lst = [
    val = root.val
    if key>val:
        find(root.right,key)
        return ['r']
    if key<val:
        find(root.left,key)
        return ['l']
    return      
        
=======
# empty list
# list of 1
# reallly long list of 1

def thing(lst):
    ind = 0 
    while ind < len(lst)-1:
        if lst[ind] == lst[ind+1]:
            lst[ind+1], lst[len(lst)-1] = lst[len(lst)-1], lst[ind]
            lst.pop()
        else:
            ind += 1
            
lst1 = []
lst2 = [1]
lst3 = [1]*10
thing(lst1)
thing(lst2)
thing(lst3)
print(lst1)
print(lst2)
print(lst3)

lst_midterm = [2,2,2,3,3,1,1,1,2,2]
thing(lst_midterm)
print(lst_midterm)
>>>>>>> 1a3a7fc (stuff)
