#q1 answer pd2752
def min_and_max(bin_tree):
    if bin_tree.is_empty():
        return None, None
    
    minmax = [bin_tree.root.data]*2
    
    def subtree_min_and_max(root):
        if root is None:
            return bin_tree.root.data, bin_tree.root.data
        if root.data < minmax[0]:
            minmax[0] = root.data
        if root.data > minmax[1]:
            minmax[1] = root.data
        subtree_min_and_max(root.left)
        subtree_min_and_max(root.right)
        return minmax[0],minmax[1]
    return subtree_min_and_max(bin_tree.root)