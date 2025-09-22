class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node.
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Skip the node with value `val`
            else:
                current = current.next  # Move to the next node

        return dummy.next  # Return the real head
