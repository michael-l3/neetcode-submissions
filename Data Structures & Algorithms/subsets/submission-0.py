class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        #keep track of the index we are doing 
        #take or not take 

        def dfs(currList,i): 
            nonlocal res

            if i >= len(nums): 
                res.append(currList.copy())
                return 
                
            number = nums[i]
            currList.append(number)
            dfs(currList,i+1)

            #dont take
            currList.pop() 
            dfs(currList, i+1)
            
        dfs([],0)
        return res