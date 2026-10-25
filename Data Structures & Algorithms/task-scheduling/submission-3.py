import heapq 
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #we are going to have to make a cooldown 
        #keep track of the most freqent task bc we need to do those first in order to be efficient 

        freq = {}

        for task in tasks: 
            if task in freq: 
                freq[task] += 1 
            else: 
                freq[task] = 1 
        
        #add all of the counts in the heap 
        heap = []
        for count in freq.values(): 
            heapq.heappush(heap,-1 * count)

        #now we need a queue and to keep track of time
        #so when the time is ready for a number (ie a task, then we can put it back in the heap)
        q = deque() 
        time = 0 
        while heap or q: 
            #check if it is ready, the first index should be the lastest one in q
            if q and q[0][1] <= time: 
                #it can go back into heap 
                task,ready_time = q.popleft() 
                heapq.heappush(heap,task * -1)
                
            #so when we pop a task off we dont put it back on until it is ready 
            if heap:
                task = -1 * heapq.heappop(heap)
            #ie 3 
            #we did one so we decrement and add the time cooldown to q 
                if task - 1 > 0:
                    q.append((task-1,time + n + 1))
            
            time += 1 
        
        return time
