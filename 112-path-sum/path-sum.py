class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, remaining = stack.pop()
            
            # If it's a leaf and remaining is 0, we found a path
            if not node.left and not node.right and remaining == 0:
                return True
            
            if node.right:
                stack.append((node.right, remaining - node.right.val))
            if node.left:
                stack.append((node.left, remaining - node.left.val))
        
        return False
