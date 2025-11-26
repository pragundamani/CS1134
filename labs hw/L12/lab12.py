from ArrayQueue import ArrayQueue

# Q1
def is_complete(root):
    if root is None:
        return True

    queue = ArrayQueue()
    queue.enqueue(root)
    seen_none = False

    while not queue.is_empty():
        node = queue.dequeue()

        if node is None:
            seen_none = True
        else:
            if seen_none:
                return False

            queue.enqueue(node.left)
            queue.enqueue(node.right)

    return True

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
