import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #we have to keep track of time and queue of when something is ready 
        #and if the time is == i, then we are ready to process it 
        #and we have to check how many of each task is in
        time = 0
        tracker = {}
        heap = []
        for task in tasks: 
            if task in tracker: 
                tracker[task] += 1 
            else: 
                tracker[task] = 1 
        
        for count in tracker.values(): 
            heapq.heappush(heap,count * -1)
        
        #time starts at 0, we just choose the most freqent one so it is efficient 
        #[(0,2,Y),(0,2,'X')]  ** scratch this lol**

        #so now we have to pop it off till there is no heap 
        #no we have to create a queue setting the time 
        time = 0 
        q = deque() 

        while heap or q: 
            time += 1 

            if heap: 
                count = 1 + heapq.heappop(heap) #addign one to the time so we know we are decrementing the task amount

                if count != 0: 
                    q.append([count,time + n])
            
            if q and q[0][1] == time:  #this is when we know it will ready and out of idle time 
                heapq.heappush(heap,q.popleft()[0])  #so we will add the count back into the heap 

        return time 
                


        
