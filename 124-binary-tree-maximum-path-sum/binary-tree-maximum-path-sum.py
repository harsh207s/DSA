# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute max path sum from left and right, ignoring negatives
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path through the current node
            current_path = node.val + left_gain + right_gain

            # Update global max_sum
            self.max_sum = max(self.max_sum, current_path)

            # Return the best single-path gain to parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
