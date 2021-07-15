# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        lst = []

        def preorder(root, lst):
            if root == None:
                return
            lst.append(root)
            preorder(root.left, lst)
            preorder(root.right, lst)

        preorder(root, lst)
        for i in range(len(lst)):
            if i == len(lst) - 1:
                lst[i].left = None
                lst[i].right = None
            else:
                lst[i].left = None
                lst[i].right = lst[i + 1]

