class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #we need to sort 
        intervals.sort() 
        res = [] 
        previous = intervals[0]

        for i in range(1, len(intervals)): 
            if previous[1] < intervals[i][0]: 
                res.append(previous)
                previous = intervals[i]
            else: 
                # newInterval = [min(previous[0], intervals[i][0]), max(previous[1], intervals[i][1])]
                # previous = newInterval 
                previous[1] = max(previous[1], intervals[i][1])
            
        
        res.append(previous) 
        return res