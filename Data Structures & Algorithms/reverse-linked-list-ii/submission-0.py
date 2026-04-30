# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        conn = dummy
        i = 1
        while i < left :
            conn = conn.next
            i += 1

        tail = conn.next
        curr = tail
        j = 1
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        conn.next = prev
        tail.next = curr
        return dummy.next