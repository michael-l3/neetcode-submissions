import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #djkstra's algo 
        #create min heap 
        #create min_times dic  and adj list to check neis 
        g = {}
        for u,v,time in times: 
            if u not in g: 
                g[u] = [] 
            g[u].append((v,time))         #where v is the node, and time is distance for u to v 
        
        min_times = {}
        minHeap = [(0,k)]

        while minHeap: 
            timeFromK,node = heapq.heappop(minHeap)

            #check first if it is in min_times bc if it is, then we already have the min distance to that node 
            if node in min_times: 
                continue 
            
            #otherwise we have to process it 
            min_times[node] = timeFromK 

            #check the neis now 
            for nei,distance in g.get(node,[]): 
                if nei not in min_times: 
                    heapq.heappush(minHeap,(timeFromK + distance,nei))
        
        if len(min_times) == n: 
            return max(min_times.values())
        else: 
            return -1



