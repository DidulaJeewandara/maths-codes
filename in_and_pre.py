class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

in_order=[9,3,15,20,7]
pre_order=[3,9,20,15,7]
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root 

root = build_tree(pre_order, in_order)
print(root)


