# lab 11
from LinkedBinaryTree import LinkedBinaryTree

def bt_even_sum(node,total=0):
    if node is None:    
        return total
    elif node%2 == 0:
        total += node
    total += bt_even_sum(node.left,total)
    total += bt_even_sum(node.right,total)
    return total

def __contains__(self,item):
    def tree_climber(node):
        if node is None:
            return False
        if node == item:
            return True
        return tree_climber(node.left) or tree_climber(node.right)
    return tree_climber(self.root)

def is_full(root):
    if root.left is None and root.right is None:
        return True
    elif root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)
    else:
        return False
    
def __add__(self, other_root):
    final_tree = LinkedBinaryTree
    final_tree.root = self.root + other_root    
    def tree_add(node=final_tree.root,self_node=self.root,other_node=other_root.root):
        sleft, sright, oleft, oright = self_node.left is not None, self_node.right is not None, other_node.left is not None, other_node.right is not None
        if sleft and oleft:
            node.left = self_node.left + other_node.left
            tree_add(node.left,self_node.left,other_node.left)
        elif sleft and not oleft:
            node.left = self_node.left
            tree_add(node.left,self_node.left,)
        elif oleft and not sleft:
            node.left = other_node.left
        
            