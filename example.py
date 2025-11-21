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
        