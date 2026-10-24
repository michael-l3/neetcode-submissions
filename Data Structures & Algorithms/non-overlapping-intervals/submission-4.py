class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removal = 0 
        intervals.sort() 
        currInterval = intervals[0]

        for interval in intervals[1:]: 
            #overlapping we need to remove
            if interval[0] < currInterval[1]: 
                removal += 1 
                currInterval = [min(currInterval[0],interval[0]),min(currInterval[1],interval[1])]
            else: 
                currInterval = interval 
        
        return removal

