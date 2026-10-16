import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create a max heap 

        heap = [] 

        for stone in stones: 
            heapq.heappush(heap,-1 * stone)
        
        heapq.heapify(heap)
        
        while len(heap) > 1: 
            heavyStone = -1* heapq.heappop(heap)
            lighterStone = -1 * heapq.heappop(heap)

            val = heavyStone - lighterStone 

            heapq.heappush(heap,-1 *val)
                
        final = -1 * heapq.heappop(heap)
        return final