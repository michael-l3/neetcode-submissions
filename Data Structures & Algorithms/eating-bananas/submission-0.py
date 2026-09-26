import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        res = max(piles)

        while l <= r: 
            hours = 0 
            k = (l+r) // 2 

            for p in piles: 
                hours += math.ceil(p/k) #round up 
            
            if hours <= h: 
                res = min(res,k)
                r = k - 1 
            else: 
                l = k + 1 
        
        return res