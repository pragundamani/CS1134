#q2 answer pd2752
def leaves_list(self):
    x = 0
    def helper(node,x):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            x = node.value
            yield x
        else:
            yield from helper(node.left,x)
            yield from helper(node.right,x)
    return list(helper(self.root,x))