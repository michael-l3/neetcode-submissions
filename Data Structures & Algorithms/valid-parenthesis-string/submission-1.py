class Solution:
    def checkValidString(self, s: str) -> bool:
        #we are going to keep track of the max and min open brackets we can have 
        leftMin = 0 
        leftMax = 0 

        #the reason we are keeping track is because ever ( needs a closing so with * we can either choose to close 
        #aggresively which can make leftMin  < 0, when in reality we can just skip so that would be why when it is 
        # < 0 we put it back to 0 
        #but if we are choosing to open and for some reason leftMax < 0, we cant recover from it )) ( scenario 

        for ch in s: 
            if ch == '(': 
                leftMin += 1 
                leftMax += 1
            elif ch == ')': 
                leftMin -= 1 
                leftMax -= 1
            else: 
                #the wild card we can always choose to open or close or ignore, so it doesnt hurt to close 
                leftMin -= 1 
                leftMax += 1
            
            if leftMin < 0: 
                leftMin = 0 
            if leftMax < 0: 
                return False 
            
        return leftMin == 0

