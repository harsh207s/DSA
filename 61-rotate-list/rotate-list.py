# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Connect tail to head (make circular list)
        tail.next = head

        # Step 3: Find new tail = (length - k % length - 1) steps from head
        k = k % length
        steps_to_new_tail = length - k - 1

        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 4: New head is next of new_tail
        new_head = new_tail.next
        new_tail.next = None  # break the circle

        return new_head
