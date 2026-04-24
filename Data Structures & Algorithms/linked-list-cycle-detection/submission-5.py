# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ##APPROACH USING HASHMAP, TAKES O(N) AFOR BOTH SPACE AND TIME COMPLEXITY
        # count={}
        # curr=head
        # while curr:
        #     if curr.val in count:
        #         count[curr.val]+=1    
        #     else:
        #         count[curr.val]=1
        #     curr=curr.next
        #     if max(count.values())>1:
        #         return True
        # return False 

        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

