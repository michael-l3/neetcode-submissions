class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #so we are going to compare stk area 
        stk = [] 
        maxArea = 0

        #will store as [position, height]
        for i, height in enumerate(heights): 
            start = i 
            while stk and stk[-1][1] > height: 
                index,h = stk.pop() 
                w = i - index 
                area = h * w 
                maxArea = max(area,maxArea)
                start = index 

            stk.append((start,height))
        
        while stk: 
            index,h = stk.pop() 
            w = len(heights) - index 
            area = w * h 
            maxArea = max(area,maxArea) 
        
        return maxArea