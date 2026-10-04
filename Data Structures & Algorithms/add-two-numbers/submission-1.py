# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode() 
        curr = d 
        carry= 0
        while l1 or l2 or carry:  
            if l1: 
                val1 = l1.val
            else: 
                val1 = 0 
            if l2: 
                val2 = l2.val
            else: 
                val2 = 0 
            
            add = val1 + val2 + carry
            carry = add // 10 
            ones = add % 10 

            newNode = ListNode(ones) 
            curr.next = newNode 
            curr = newNode

            if l1:
                l1 = l1.next
            else: 
                l1 = None 
            if l2: 
                l2 = l2.next
            else: 
                l2 = None  
        
        return d.next
            
