class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Max money if we rob this node
            rob_this = node.val + left[1] + right[1]
            # Max money if we don't rob this node
            not_rob_this = max(left) + max(right)
            
            return (rob_this, not_rob_this)
        
        return max(dfs(root))

# Example usage:
# root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(1))
# solution = Solution()
# print(solution.rob(root))  # Output: 7