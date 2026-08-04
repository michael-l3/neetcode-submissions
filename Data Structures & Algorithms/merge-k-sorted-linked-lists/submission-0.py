# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create a min heap 
        #iterate through the list to add the first node of the linked list 
        #then go through each one and add the index too so that it has ranking 

        heap = [] 

        for i, node in enumerate(lists):
            if node:  
                heapq.heappush(heap,(node.val,i,node))
        
        dummy = ListNode() 
        curr = dummy 

        while heap: 
            val,i,node = heapq.heappop(heap)
            curr.next = node 
            curr = node 
            node = node.next  

            if node: 
                heapq.heappush(heap,(node.val,i,node))
        
        return dummy.next

