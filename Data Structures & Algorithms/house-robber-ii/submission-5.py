class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
            
        def rob2(nums):
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
        
        return max(rob2(nums[0:len(nums) - 1]),rob2(nums[1:]))