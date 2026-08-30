class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        previous = intervals[0]

        res = [] 

        for i in range(1, len(intervals)): 
            if previous[1] < intervals[i][0]: 
                res.append(previous)
                previous = intervals[i]
            else: 
                newInterval = [min(previous[0],intervals[i][0]), max(previous[1],intervals[i][1])]
                previous = newInterval
        
        res.append(previous)
        return res