# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we can use fast and slow in order to find the node right before the drop
        d = ListNode() 
        d.next = head 
        slow = d 
        fast = d

        for _ in range(n): 
            fast = fast.next 
        
        while fast and fast.next: 
            fast = fast.next 
            slow = slow.next
        
        slow.next = slow.next.next 

        return d.next
        

        
