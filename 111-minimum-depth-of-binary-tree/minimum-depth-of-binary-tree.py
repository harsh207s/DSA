# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If no left child, go down right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If no right child, go down left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children exist, take the shorter one
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
