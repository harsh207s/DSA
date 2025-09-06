# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # Two pointers
        pA, pB = headA, headB
        
        # Traverse until they meet or both hit None
        while pA != pB:
            # Move each pointer; if it reaches the end, redirect to the other list
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA   # Either intersection node or None
