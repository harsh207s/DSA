class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):  # first time at this depth
                res.append(node.val)
            # go right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
