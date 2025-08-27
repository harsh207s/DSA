from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            # Check if there are at least k nodes left
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next

            # Reverse k nodes
            curr = prev.next
            nxt = curr.next
            for _ in range(k - 1):
                temp = nxt.next
                nxt.next = curr
                curr = nxt
                nxt = temp

            # Connect reversed group with rest of the list
            tail = prev.next
            prev.next.next = nxt
            prev.next = curr
            prev = tail
