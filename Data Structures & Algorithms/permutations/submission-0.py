class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        visted = set() 

        def dfs(curr): 
            if len(curr) == len(nums): 
                res.append(curr.copy())
                return 
            
            #now iterate thru the numbers 
            for number in nums: 

                if number in visted: 
                    continue 
                
                #take/choose the number 
                visted.add(number)
                curr.append(number)
                dfs(curr)

                #after hit base case then we pop it off and get it off of set too 
                curr.pop()
                visted.remove(number)
        

        dfs([])
        return res