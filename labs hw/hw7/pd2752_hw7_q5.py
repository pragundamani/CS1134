#q5 answer pd2752
from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    tokens = prefix_exp_str.split()
    
    def helper(prefix_exp,start):
        if start>=len(prefix_exp):
            return None,0
        
        token = prefix_exp[start]
        
        if token in ['+','-','*','/']:
            node = LinkedBinaryTree.Node(token)
            
            left,left_size = helper(prefix_exp,start+1)
            right,right_size = helper(prefix_exp,start+1+left_size)
            node.left = left
            if left is not None:
                left.parent = node
            node.right = right
            if right is not None:
                right.parent = node
            return node,1+left_size+right_size
        else:
            node = LinkedBinaryTree.Node(int(token))
            return node,1
    
    root_node,x = helper(tokens,0)
    return LinkedBinaryTree(root_node)

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    result = []
    
    def postorder(root):
        if root is not None:
            postorder(root.left)
            postorder(root.right)
            result.append(str(root.data))
    
    postorder(tree.root)
    return ' '.join(result)
