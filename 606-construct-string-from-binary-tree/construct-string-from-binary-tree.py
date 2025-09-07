# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        # If no children, just return value
        if not root.left and not root.right:
            return str(root.val)

        # If only left child exists
        if root.left and not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"

        # If right child exists, we must include parentheses for left (even if it's empty)
        if not root.left and root.right:
            return str(root.val) + "()" + "(" + self.tree2str(root.right) + ")"

        # If both children exist
        return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"
