class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #this is a greedy approach we will have to compare the last value 
        #sort it so that it is in asending order first based oin the first value 

        intervals.sort() 
        res = 0 
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]: 
            if prevEnd <= start: 
                prevEnd = end 
            else: 
                res += 1 
                prevEnd = min(prevEnd, end)
        
        return res