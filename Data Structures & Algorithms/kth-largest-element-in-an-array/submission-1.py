import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using a minHeap 
        minHeap = [] 

        for number in nums: 
            heapq.heappush(minHeap,number)
        
        while len(minHeap) > k: 
            heapq.heappop(minHeap)
        
        return minHeap[0]