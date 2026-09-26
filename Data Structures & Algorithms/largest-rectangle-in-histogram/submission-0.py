class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #so we are going to compare stk area 
        stk = [] 
        max_area = 0

        #will store as [position, height]
        for i, height in enumerate(heights): 
            start = i
            while stk and stk[-1][1] > height: 
                index,height_popped = stk.pop() 
                w = i - index
                area = w * height_popped 
                max_area = max(max_area,area)
                start = index
            
            stk.append((start,height))
        
        while stk: 
            index,height_popped = stk.pop() 
            w = len(heights) - index 
            area = height_popped * w 
            max_area = max(max_area,area)
        
        return max_area
