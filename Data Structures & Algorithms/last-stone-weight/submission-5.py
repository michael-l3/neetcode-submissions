import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create a max heap, then keep smashing and readding till the len(stone) == 1 

        heap = []

        for stone in stones: 
            heapq.heappush(heap,stone * -1)
        
        heapq.heapify(heap)

        #so now we have a maxHeap 
        while len(heap) > 1: 
            bigStone = heapq.heappop(heap) * -1 
            smallStone = heapq.heappop(heap) * -1 

            newStone = bigStone - smallStone 

            heapq.heappush(heap,newStone * -1)
        
        if heap: 
            return -heap[0]
        else: 
            return 0