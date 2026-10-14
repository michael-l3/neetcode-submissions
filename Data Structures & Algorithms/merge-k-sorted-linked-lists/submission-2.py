# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #use minheap in order to do this 
        heap = [] 

        for i,node in enumerate(lists): 
            if node: 
                heapq.heappush(heap,(node.val,i,node))
        
        #now we have the beginning of each node in this min heapn 
        d = ListNode()
        curr = d 

        while heap: 
            val,i,node = heapq.heappop(heap)
            curr.next = node
            curr = node 

            if node.next: 
                node = node.next
                heapq.heappush(heap,(node.val,i,node)) 
        
        return d.next