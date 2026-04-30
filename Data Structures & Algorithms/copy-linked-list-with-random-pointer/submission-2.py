"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        oldTonew = {}

        while curr:
            oldTonew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            oldTonew[curr].next = oldTonew.get(curr.next)
            oldTonew[curr].random = oldTonew.get(curr.random)
            curr = curr.next

        return oldTonew[head]        
        