# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        result = []
        self.BST(root, result)
        first = None
        second = None
        for i in range(1, len(result)):
            if (result[i - 1].val >= result[i].val):
                if first == None:
                    first = i - 1
                    second = i
                else:
                    second = i
        result[first].val, result[second].val = result[second].val, result[first].val

    def BST(self, root, result):
        if root == None:
            return True
        self.BST(root.left, result)
        result.append(root)
        self.BST(root.right, result)
