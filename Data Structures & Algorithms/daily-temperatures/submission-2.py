class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] 
        res = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp: 
                stk_index,stk_temp = stk.pop() 
                res[stk_index] = i - stk_index

            stk.append((i,temp)) 
        
        return res
