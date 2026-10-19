from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        level = [] 

        #helping function to tell if it is a partition or not 
        def is_palidrome(l,r): 
            while l < r: 
                if s[l] != s[r]: 
                    return False 
                
                l += 1 
                r -= 1  

            return True
            
        
        def dfs(i): 
            if i >= len(s): 
                res.append(level.copy())
                return 
            
            for j in range(i,len(s)): 
                if is_palidrome(i,j): 
                    level.append(s[i:j+1])
                    dfs(j+1)
                    level.pop()


        dfs(0)
        return res