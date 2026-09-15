class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removal = 0 

        intervals.sort() 

        #should be [1,2], [1,4], [2,4]
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]: 
            if start >= prevEnd: 
                prevEnd = end
            else: 
                removal += 1 
                prevEnd = min(prevEnd,end)
        
        return removal