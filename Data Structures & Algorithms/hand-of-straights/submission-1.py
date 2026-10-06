from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0: 
            return False 
        
        #we need to count the amount of times each of them are in hands in a dictionary 
        d = {} 

        for number in hand: 
            if number in d: 
                d[number] += 1
            else: 
                d[number] = 1 
        
        #so now we have the amount of times it shows up 

        #so while our dictionary exist, if we go thru we capture the min number then go up to that + group num 
        # to fill out the group
        while d: 
            minVal = min(d)

            for number in range(minVal,minVal + groupSize): 
                if number not in d: 
                    return False 
                
                d[number] -= 1 

                if d[number] == 0: 
                    del d[number]
        
        return True