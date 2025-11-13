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