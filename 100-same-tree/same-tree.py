# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, trees are identical
        if not p and not q:
            return True
        # If one is None, but not the other
        if not p or not q:
            return False
        # If values differ
        if p.val != q.val:
            return False
        # Recursively check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
