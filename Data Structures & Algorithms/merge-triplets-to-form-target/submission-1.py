from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = [0, 0, 0]

        for triplet in triplets: 
            
            #These three scenarios is because we have overshot the target value so it would never work
            if triplet[0] > target[0]: 
                continue 
            if triplet[1] > target[1]: 
                continue 
            if triplet[2] > target[2]: 
                continue 
            
            temp[0] = max(triplet[0],temp[0])
            temp[1] = max(triplet[1],temp[1])
            temp[2] = max(triplet[2],temp[2])
        
        #now we check if we made it 
        return temp == target