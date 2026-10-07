class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #so we will have to build a hashmap to contain the last index of that character 
        h = {} 

        for i , c in enumerate(s): 
            h[c] = i 
        
        res = [] 
        size = 0 
        end = 0
        for i, c in enumerate(s): 
            size += 1 
            end = max(end,h[c])

            #reset the size and res bc we found a partition that only contains those specific values
            if i == end: 
                res.append(size)
                size = 0 
        
        return res
