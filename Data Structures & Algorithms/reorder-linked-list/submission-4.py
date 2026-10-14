# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #will have to use fast and slow to find the mid point 
        fast = head 
        slow = head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        #at this point slow.next will be the turning point 
        curr = slow.next 
        prev = None 
        slow.next = None 

        #reverse the second side 
        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        
        #[0,1,2,3,None]  and [6,5,4,None]
        l1 = head 
        l2 = prev 

        while l2: 
            temp1 = l1.next 
            temp2 = l2.next 
            l1.next = l2
            l2.next = temp1 
            l1 = temp1
            l2 = temp2
