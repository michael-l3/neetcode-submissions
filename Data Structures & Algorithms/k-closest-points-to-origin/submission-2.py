import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #so we are going to make a min heap based on distance and the points 
        heap = []

        for x,y in points: 
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(heap,(distance,x,y))
        
        heapq.heapify(heap)

        res = [] 

        for _ in range(k): 
            distance,x,y = heapq.heappop(heap)
            res.append([x,y])
        
        return res