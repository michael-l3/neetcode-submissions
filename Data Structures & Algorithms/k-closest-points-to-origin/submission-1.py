import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #store the distance first then the points as tuple so something like this: [10,(x,y)]
        minHeap = [] 
        res = []
        for x,y in points: 
            distance = math.sqrt((x-0)**2 +(y-0)**2)
            heapq.heappush(minHeap,(distance,x,y))
        
        for _ in range(k): 
            distance,x,y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res
        

