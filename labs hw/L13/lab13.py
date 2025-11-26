from BinarySearchTreeMap import BinarySearchTreeMap
# lab 13
#
def min_max(bst):
    if bst.is_empty():
        return None, None
    node = bst.root
    while node.left is not None:
        node = node.left
    min_key = node.item.key
    node = bst.root
    while node.right is not None:
        node = node.right
    max_key = node.item.key
    return (min_key, max_key)

def greater_equal_n(bst,n):
    node = bst.root
    if node is None:
        return 0
    bst_max = int('-inf')
    while node.right is not None and node.item.key > bst_max:
        bst_max = node
        node = node.right
    return bst_max
        
def bst_copy_check(bst1,bst2):
    if bst1.is_empty() and bst2.is_empty():
        return True
    elif bst1.is_empty() or bst2.is_empty():
        return False
    if len(bst1) != len(bst2):
        return False
    def node_check(item):
        if bst2.find_node(item) is None:
            return False
        return True
    for i in bst1.inorder():
        if not node_check(i):
            return False
        
def 