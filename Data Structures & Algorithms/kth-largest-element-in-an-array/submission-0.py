import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #minHeap and keep removing until we get k element 

        heap = nums 
        heapq.heapify(heap)

        while len(heap) > k: 
            heapq.heappop(heap)
        
        return heap[0]
