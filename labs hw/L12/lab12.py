# from ArrayQueue import ArrayQueue

# Q1
def is_complete(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    elif root.left is not None and root.right is not None:
        return is_complete(root.left) and is_complete(root.right)
    else:
        return False

# Q2
def clean_subtree(root):
    if root is None:
        return None
    root.left = clean_subtree(root.left)
    root.right = clean_subtree(root.right)
    if root.data != 1 and root.left == None and root.right == None:
        return None
    return root


# Q3
def count_paths_exceeding_threshold(root, threshold):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if root.data > threshold:
            return 1
        else:
            return 0
    return count_paths_exceeding_threshold(root.left, threshold-root.data) + count_paths_exceeding_threshold(root.right, threshold-root.data)