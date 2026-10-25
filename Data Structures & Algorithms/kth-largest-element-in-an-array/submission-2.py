import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #make a min heap 
        heap = []

        for number in nums: 
            heapq.heappush(heap,number)
        
        heapq.heapify(heap)

        while len(heap) > k: 
            heapq.heappop(heap)
        
        return heap[0]