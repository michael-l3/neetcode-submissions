# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #we would use slow and fast pointer in order to find the midpoint 
        #slow.next would be where the second halve starts 
        #so we would be using 

        fast = head 
        slow = head 

        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 

        #now slow.next will be the midpoint of what we are doing 
        #reverse the link list none
        prev = None
        curr = slow.next 
        slow.next = None 

        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        
        #now we have something like this [0,1,2,3] [6,5,4] 
        #now we just need to merge the two together 
        list1 = head 
        list2 = prev 


        while list2: 
            temp1 = list1.next 
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1 
            list1 = temp1 
            list2 =  temp2


