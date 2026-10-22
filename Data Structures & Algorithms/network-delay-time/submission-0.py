import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #djkstra's algo 
        #use a minHeap to pop 
        #create an adj list 
        g = {} 

        for u , v, time in times: 
            if u not in g: 
                g[u] = []
            g[u].append((v,time))
        #so now we have our list 
        min_times = {} #keep track of the minimum times it takes to get to a certain node 
        minHeap = [(0,k)]   #where(distances from k,node that we are at)

        while minHeap:
            timeFromK,node = heapq.heappop(minHeap)
            #check if we already vistied, if we have then we know that this isnt min distance 
            if node in min_times: 
                continue 
            
            #otherwise we log
            min_times[node] = timeFromK
            
            #now we check the neis 
            for nei,distance in g.get(node,[]): 
                if nei not in min_times: 
                    heapq.heappush(minHeap,(timeFromK + distance,nei))
        
        if len(min_times) == n:  #this means that I could visit all of the nodes
            return max(min_times.values())
        else: 
            return -1

