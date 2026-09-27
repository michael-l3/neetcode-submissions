class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [] 
        level = [] 

        def dfs(i, curr, total): 
            if total == target: 
                res.append(curr.copy())
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            #take 
            number = candidates[i]
            curr.append(number)
            dfs(i+1,curr,total + number)

            #too big or dont take that specific number
            curr.pop() 

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: 
                i += 1 
            
            dfs(i + 1,curr,total)



        dfs(0,[],0)
        return res