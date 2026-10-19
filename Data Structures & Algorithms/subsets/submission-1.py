class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(i,currLevel):  #where currLevel is the array that we currently have
            if i >= len(nums): 
                res.append(currLevel.copy())
                return 
            
            #need to take the currNumber and move onto the next 
            currLevel.append(nums[i])
            dfs(i+1,currLevel)
            #remove the number now 
            currLevel.pop() 

            #scenario where we dont take the number 
            dfs(i+1,currLevel)

        
        
        dfs(0,[])
        return res