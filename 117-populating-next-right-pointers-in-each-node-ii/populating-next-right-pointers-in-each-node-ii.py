"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Start with the root
        curr = root

        while curr:
            dummy = Node(0)  # Dummy node for the next level
            tail = dummy

            # Traverse current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next  # Move to next node in current level

            # Move to the first node of the next level
            curr = dummy.next

        return root
