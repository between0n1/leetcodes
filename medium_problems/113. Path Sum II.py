# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # do DFS
        # each node, update Sum and path
        # when node == none, append path to the result
        result = []
        path = []

        def DFS(root, targetSum, path, result):
            if root == None:
                return
            if root.left == None and root.right == None:
                if targetSum == root.val:
                    result += [path + [root.val]]

                return
            else:
                DFS(root.left, targetSum - root.val, path + [root.val], result)
                DFS(root.right, targetSum - root.val, path + [root.val], result)

        DFS(root, targetSum, [], result)
        return result
        #         def DFS(root, targetSum, path, result):
#             if root == None:
#                 if targetSum == 0:
#                     if result[len(result)]
#                     result += [path]
#                 return
#             else:
#                 DFS(root.left, targetSum - root.val, path + [root.val], result)
#                 DFS(root.right, targetSum - root.val, path + [root.val], result)
