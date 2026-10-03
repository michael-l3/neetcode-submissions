# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create a minheap that also has index
        #the the nodes on the heap and the value  

        heap = [] 

        for i,node in enumerate(lists): 
            if node:    
                heapq.heappush(heap,(node.val,i,node))
        
        #would look like [(1,1,node1),(1,2,node.2),(3,3,node.3)]
        #now we pop and add to res  
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