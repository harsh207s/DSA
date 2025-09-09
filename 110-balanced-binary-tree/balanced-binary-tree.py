# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0  # height of empty tree is 0

            left = dfs(node.left)
            if left == -1:
                return -1  # left subtree not balanced

            right = dfs(node.right)
            if right == -1:
                return -1  # right subtree not balanced

            if abs(left - right) > 1:
                return -1  # current node not balanced

            return 1 + max(left, right)  # return height

        return dfs(root) != -1
