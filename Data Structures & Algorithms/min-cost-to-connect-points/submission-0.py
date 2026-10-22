
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #going to have a minHeap that stores (distance to that point, index of that point)
        #we iterate thru the points and create the distance value 
        #we continue to pop until all of the points have been visted via stored in a set 
        minHeap = [(0,0)] #cost nothing to start 
        visted = set() 
        res = 0

        while len(visted) < len(points): #this is how we will know if all points are visited 
            cost, point = heapq.heappop(minHeap)

            if point in visted: 
                continue

            visted.add(point)
            res += cost 

            x1,y1 = points[point] 

            #now we have to connect everything to this and only take the smallest one via minheap 
            for other_point in range(len(points)): 
                if other_point not in visted: 
                    x2,y2 = points[other_point] 

                    distance = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minHeap,(distance,other_point)) 
        
        return res