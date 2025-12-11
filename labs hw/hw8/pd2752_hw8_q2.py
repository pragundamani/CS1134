# q2 answer pd2752
import BinarySearchTreeMap


def create_chain_bst(n):
    restree = BinarySearchTreeMap.BinartSearchTreeMap()
    if n < 1:
        return restree
    for i in range(n):
        restree.insert(i + 1, i + 1)
    return restree


def create_complete_bst(n):
    bst = BinarySearchTreeMap.BinartSearchTreeMap()
    root = n//2 + 1
    
    bst.insert(root,root)
    
    if n < 0:
        return bst

    def add_items(tree,low,high):
        if low > high:
            return
        mid = (low+high)//2
        if mid != root:
            tree.insert(mid,mid)
        add_items(tree,low, mid-1)
        add_items(tree,mid+1,high)    
    
    add_items(bst, 1, n)
    return bst
