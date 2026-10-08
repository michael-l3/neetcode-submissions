class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0 
        r = len(heights) - 1 

        while l < r: 
            height = min(heights[l],heights[r])
            w = r - l 
            area = height * w 

            maxArea = max(maxArea,area)

            if heights[l] < heights[r]: 
                l += 1 
            else: 
                r -= 1 
        
        return maxArea