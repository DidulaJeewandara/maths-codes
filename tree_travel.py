from logging import root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        self.inorder_helper(root, result)
        return result
    
    def inorder_helper(self, node, result):
        if node:
            self.inorder_helper(node.left, result)
            result.append(node.val)
            self.inorder_helper(node.right, result)

    def preorderTraversal(self, root):
        result2 = []
        self.preorder_helper(root, result2)
        return result2
   
    def preorder_helper(self, node, result2):

        if node:
            result2.append(node.val)
            self.preorder_helper(node.left,result2)
            self.preorder_helper(node.right,result2)
 

    def postorderTraversal(self, root):
        result3 = []
        self.postorder_helper(root, result3)
        return result3
    
    def postorder_helper(self, node, result3):
        if node:
            self.postorder_helper(node.left, result3)
            self.postorder_helper(node.right, result3)
            result3.append(node.val)


    def build_tree(self,list):
        if not list:
            return None

        root=TreeNode(list[0])
        queue=[root]
        i=1
        while queue and i<len(list):
            current=queue.pop(0)

            if list[i] is not None:
                current.left=TreeNode(list[i])
                queue.append(current.left)
            i+=1

            if i<len(list) and list[i] is not None:
                current.right=TreeNode(list[i])
                queue.append(current.right)
            i+=1

        return root
class main:

    list=[1,2,3,None,4,None,5]
    Solution=Solution() 
    root=Solution.build_tree(list)
    preorder=Solution.preorderTraversal(root)
    inorder=Solution.inorderTraversal(root)
    postorder=Solution.postorderTraversal(root)
    print("Preorder:", preorder)
    print("Inorder:", inorder)
    print("Postorder:", postorder)
  
