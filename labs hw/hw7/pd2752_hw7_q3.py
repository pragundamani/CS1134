#q3 answer pd2752
def is_height_balanced(bin_tree):
    if bin_tree.is_empty():
        return True
    
    def recursive_helper(root):
        if root is None:
            return (0, True)
        
        lheight,left_balanced = recursive_helper(root.left)
        rheight,right_balanced = recursive_helper(root.right)
        if lheight>rheight:
            curr = 1+lheight
            height_diff = lheight-rheight
        else:
            curr = 1+rheight
            height_diff = rheight-lheight
        is_current_balanced = height_diff <=1
        balanced = (left_balanced and right_balanced) and is_current_balanced
        return (curr,balanced)
    
    x,balanced = recursive_helper(bin_tree.root)
    return balanced