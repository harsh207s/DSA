class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next   # store next node
            current.next = prev        # reverse the link
            prev = current             # move prev forward
            current = next_node        # move current forward

        return prev  # new head of reversed list
