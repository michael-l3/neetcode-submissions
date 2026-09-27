import heapq 
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Create a maxHeap in order ot keep track of the most frequenet task bc we need to do them first 
        count = Counter(tasks)
        heap = []

        for values in count.values(): 
            heapq.heappush(heap,values * -1)
        
        q = deque() 
        time = 0 

        while heap or q: 
            #always increment the time by one regardless(we will either be idle or doing task)
            time += 1 
            if heap: 
                counter = heapq.heappop(heap)
                counter += 1 

                if counter != 0: 
                    q.append((counter,time + n)) #this is how we know it is off cool down 
            
            if q and q[0][1] == time: 
                counter, _ = q.popleft()
                heapq.heappush(heap,counter)
        
        return time
        

