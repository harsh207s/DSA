class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Step 1: move `prev` to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse from `left` to `right`
        curr = prev.next
        prev_sub = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_sub
            prev_sub = curr
            curr = nxt

        # Step 3: reconnect
        prev.next.next = curr     # tail of reversed sublist connects to `curr`
        prev.next = prev_sub      # prev connects to new head of sublist

        return dummy.next
