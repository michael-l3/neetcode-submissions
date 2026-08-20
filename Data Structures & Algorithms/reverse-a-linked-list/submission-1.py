# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we are reversing so we have to keep track of everything 
        prev = None 
        curr = head 

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp 
        
        return prev