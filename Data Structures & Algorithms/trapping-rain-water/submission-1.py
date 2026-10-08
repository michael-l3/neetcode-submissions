class Solution:
    def trap(self, height: List[int]) -> int:
        #so we compare the heights and left nad heights at right 
        #and based on that we know what to compare because that will always be the limiting factor to how much water 
        #you can capture 

        capture = 0 
        l = 0 
        r = len(height) - 1 
        maxL = 0 
        maxR = 0 

        while l < r: 
            if height[l] <= height[r]: 
                if height[l] >= maxL: 
                    maxL = height[l]
                else: 
                    capture += maxL - height[l]
                
                l += 1 

            else:
                if height[r] >= maxR: 
                    maxR = height[r]
                else: 
                    capture += maxR - height[r]
                
                r -= 1

        return capture 
