# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index in inorder for O(1) lookup
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the last index in postorder (root is at the end in postorder)
        self.post_idx = len(postorder) - 1

        def helper(left: int, right: int) -> Optional[TreeNode]:
            # if there are no elements to construct the tree
            if left > right:
                return None

            # Pick current root from postorder
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)

            # Move to the next root (towards left in postorder)
            self.post_idx -= 1

            # Build right subtree first (because postorder is left → right → root,
            # so when we go backwards, we process root → right → left)
            root.right = helper(inorder_index_map[root_val] + 1, right)
            root.left = helper(left, inorder_index_map[root_val] - 1)

            return root

        return helper(0, len(inorder) - 1)
