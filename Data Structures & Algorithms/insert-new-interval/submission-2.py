class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals: 
            if newInterval[0] > interval[1]: 
                res.append(interval)
            elif interval[0] > newInterval[1]: 
                res.append(newInterval)
                newInterval = interval 
            else: 
                newInterval = [min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
        
        res.append(newInterval)
        return res