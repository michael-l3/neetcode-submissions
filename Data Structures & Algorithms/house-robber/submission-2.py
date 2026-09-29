class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i): 
            if i >= len(nums): 
                return 0
            
            if i in memo: 
                return memo[i]
            
            #you cant rob two adjacent houses
            firstHouse = dfs(i+2)
            secondHouse = dfs(i+1)

            #max between robbing two or just robbing that house
            memo[i] = max(firstHouse + nums[i], secondHouse)
            return memo[i]
        
        return dfs(0)