# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Insert copied nodes after each original node
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # Step 2: Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the original and copied nodes
        old = head
        new_head = head.next
        new = new_head
        while old:
            old.next = old.next.next
            if new.next:
                new.next = new.next.next
            old = old.next
            new = new.next
        
        return new_head
