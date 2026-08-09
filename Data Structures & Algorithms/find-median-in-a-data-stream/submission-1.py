class MedianFinder:

    def __init__(self):
        self.small = [] 
        self.large = []

    def addNum(self, num: int) -> None:
        #we will always be pushing the num to small first 
        heapq.heappush(self.small,-1 * num)

        #now make sure that if there is a large and small that small
        #only contains number that are less that those in small
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = heapq.heappop(self.small) * - 1 
            #now add it to the large heap 
            heapq.heappush(self.large, val)
        
        #okay now we have to balance out the two 
        if len(self.small) > len(self.large) + 1: 
            val = heapq.heappop(self.small) * -1 
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) 
            #correct the value
            heapq.heappush(self.small, -1 * val) 

            #now we have balance data structure 

    def findMedian(self) -> float:
        #so if it is balanced whichever one is greater that the top 
        #of the stack is the median, otherwise we calculate it 
        if len(self.small) > len(self.large): 
            return self.small[0] * -1 
        elif len(self.small) < len(self.large): 
            return self.large[0]
        else: 
            #compute median 
            median = ((self.small[0]*-1) + self.large[0]) / 2
            return median
        
        