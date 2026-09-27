import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create a max heap and keep smashing the stones together 

        heap = [] 

        #create max heap 
        for i in range(len(stones)): 
            heapq.heappush(heap, stones[i] * - 1)
        
        while len(heap) > 1: 
            heavierStone = heapq.heappop(heap) * -1
            lighterStone = heapq.heappop(heap) * -1

            newStone = heavierStone - lighterStone 

            heapq.heappush(heap,newStone * -1)
        
        return heap[0] * -1


