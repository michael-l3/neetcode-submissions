class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stk = [] 

        for i, temp in enumerate(temperatures): 
            while stk and stk[-1][1] < temp: 
                stk_i, stk_t = stk.pop() 
                res[stk_i] = i - stk_i 

            stk.append((i,temp))
        
        return res