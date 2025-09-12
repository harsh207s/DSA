from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Dummy node
        curr = head  # Current node to be inserted

        while curr:
            prev = dummy
            next_temp = curr.next  # Store next node to be processed

            # Find correct place to insert current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Move to the next node in the input list
            curr = next_temp

        return dummy.next
