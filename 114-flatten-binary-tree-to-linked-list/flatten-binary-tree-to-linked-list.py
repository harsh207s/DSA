# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return None
            
            # Flatten left and right subtrees
            left_tail = helper(node.left)
            right_tail = helper(node.right)

            # If there is a left subtree, we shuffle connections
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # Return the tail of the flattened tree
            return right_tail or left_tail or node
        
        helper(root)
