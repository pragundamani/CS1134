#q1 answer pd2752
def subtree_min_and_max(bin_tree):
    if bin_tree.is_empty():
        return None, None
    
    minmax = [float('inf'), float('-inf')]
    
    def recursive_helper(root):
        if root is None:
            return None,None
        if root.data < minmax[0]:
            minmax[0] = root.data
        if root.data > minmax[1]:
            minmax[1] = root.data
        recursive_helper(root.left)
        recursive_helper(root.right)
        return min,max
    return recursive_helper(bin_tree.root)

