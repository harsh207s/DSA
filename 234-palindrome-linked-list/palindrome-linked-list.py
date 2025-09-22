class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle (slow will point to mid)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare both halves
        left, right = head, prev
        while right:  # only need to check till right ends (shorter half)
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
