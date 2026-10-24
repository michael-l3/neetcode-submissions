class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Start with a dummy accumulator of [0, 0, 0]
        curr = [0, 0, 0]

        for t in triplets:
            # If any element in the triplet exceeds the target, 
            # merging it would ruin our chances. Skip it!
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # Otherwise, safely merge it by taking the max
            curr = [
                max(curr[0], t[0]),
                max(curr[1], t[1]),
                max(curr[2], t[2])
            ]
            
            # If our accumulated merge matches the target, we're done!
            if curr == target:
                return True
    
        return curr == target