#q3 answer pd2752
from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    
    if not prefix_lst:
        return bst
    n = len(prefix_lst)

    def helper(index,low,high):
        if index>=n:
            return None, index
    
        temp = prefix_lst[index]
        if not (low<temp<high):
            return None, index
    
        item = BinarySearchTreeMap.Item(temp)
        node = BinarySearchTreeMap.Node(item)
        index += 1
        node.left, index = helper(index,low,temp)
    
        if node.left:
            node.left.parent = node
        node.right, index = helper(index,temp,high)
    
        if node.right:
            node.right.parent = node
        return node, index
    
    bst.root, temp2 = helper(0, float('-inf'), float('inf'))
    bst.n = n
    return bst
