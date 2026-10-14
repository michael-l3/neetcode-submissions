# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode() 
        d.next = head
        slow = d 
        fast = d 

        for _ in range(n): 
            fast = fast.next 
        
        while fast and fast.next: 
            fast = fast.next 
            slow = slow.next 
        
        #now slow will just skip the next value 
        slow.next = slow.next.next 
        
        return d.next