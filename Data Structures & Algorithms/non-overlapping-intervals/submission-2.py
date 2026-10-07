class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        prevMax = intervals[0][1]
        removal = 0 

        for interval in intervals[1:]: 
            if interval[0] < prevMax: 
                removal += 1 
                prevMax = min(prevMax,interval[1])
            else: 
                prevMax = interval[1]
        
        return removal


