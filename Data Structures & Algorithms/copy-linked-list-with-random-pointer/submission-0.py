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
        OldToNew = {}

        while curr:
            OldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            OldToNew[curr].next = OldToNew.get(curr.next)
            OldToNew[curr].random = OldToNew.get(curr.random)
            curr = curr.next
        
        return OldToNew[head]
        