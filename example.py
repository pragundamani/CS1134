from LinkedBinaryTree import LinkedBinaryTree

def tree_sum(tree):
    total = 0
    def child_sum(tree,the_node):
        total += the_node.data
        if the_node.left != None:
            child_sum(tree,the_node.left)
        if the_node.right != None:
            child_sum(tree,the_node.right)
    child_sum(tree,tree.root)

    return total

def level_sum(tree, level):
    def level_helper(node, current_level):
        if node is None:
            return 0
        if current_level == level:
            return node.data
        else:
            return (level_helper(node.left, current_level + 1) +
                    level_helper(node.right, current_level + 1))
    
    return level_helper(tree.root, 0)

