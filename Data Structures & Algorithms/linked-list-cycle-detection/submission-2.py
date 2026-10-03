# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using khans algo in order ot do so 
        #fast and slow pointer nad if they = each other then there is a cycle 
        d = ListNode() 
        d.next = head
        fast = d
        slow = d

        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
        
            if fast == slow: 
                return True 
        
        return False