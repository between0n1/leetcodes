# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS validate -> inorder
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        self.BST(root, result)
        for i in range(1, len(result)):
            if (result[i - 1] >= result[i]):
                return False
        return True

    def BST(self, node, result):
        if node == None:
            return True

        self.BST(node.left, result)
        result.append(node.val)
        self.BST(node.right, result)