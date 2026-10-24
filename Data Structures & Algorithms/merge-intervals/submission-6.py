class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        res = [] 
        currInterval = intervals[0]

        for interval in intervals[1:]: 
            if currInterval[1] < interval[0]: 
                res.append(currInterval)
                currInterval = interval 
            else: 
                currInterval = [min(currInterval[0],interval[0]),max(currInterval[1],interval[1])] 
        
        res.append(currInterval)
        return res