# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index in inorder for O(1) lookup
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Keep track of root index in preorder
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            # if there are no elements to construct the tree
            if left > right:
                return None

            # Pick up pre_idx element as a root
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)

            # Root is picked, increment pre_idx
            self.pre_idx += 1

            # Build left and right subtree
            # Excluding inorder_index_map[root_val] element because it's the root
            root.left = helper(left, inorder_index_map[root_val] - 1)
            root.right = helper(inorder_index_map[root_val] + 1, right)

            return root

        return helper(0, len(inorder) - 1)
