class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        currInterval = intervals[0]
        res = [] 

        for interval in intervals[1:]: 
            if interval[0] > currInterval[1]: 
                res.append(currInterval)
                currInterval = interval 
            else: 
                currInterval = [min(currInterval[0],interval[0]),max(currInterval[1],interval[1])]
        
        res.append(currInterval)
        return res