class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [] 
        level = [] 

        def dfs(i, currSum): 
            if currSum == target: 
                res.append(level.copy()) 

            if i >= len(candidates): 
                return 
            
            for j in range(i,len(candidates)): 
                if j > i and candidates[j] == candidates[j-1]: 
                    continue 
                
                if currSum + candidates[j] > target: 
                    break 
                
                number = candidates[j]
                level.append(number)
                dfs(j+1, currSum + candidates[j])

                level.pop() 

        dfs(0,0)
        return res