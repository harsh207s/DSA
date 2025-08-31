class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)       # left
            res.append(node.val)     # root
            inorder(node.right)      # right

        inorder(root)
        return res
