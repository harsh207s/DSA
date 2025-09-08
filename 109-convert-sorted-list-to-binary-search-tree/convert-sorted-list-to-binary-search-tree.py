class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Convert linked list to array for easier access
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # Recursive function to build BST from array
        def buildBST(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root

        return buildBST(0, len(values) - 1)
