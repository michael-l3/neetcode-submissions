class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # Fixed: check against groupSize instead of 2
        if len(hand) % groupSize != 0: 
            return False 
        
        # Create dictionary with counts
        d = {}
        for number in hand: 
            if number in d: 
                d[number] += 1 
            else: 
                d[number] = 1
            
        smallest = min(d)
        curr_group = 0
        while d: 
            curr_group += 1
            d[smallest] -= 1 
            if d[smallest] == 0: 
                del d[smallest]
            
            if curr_group == groupSize: 
                # Safety check: if dictionary is now empty, we are done!
                if not d:
                    break
                smallest = min(d)
                curr_group = 0
                continue
                
            nextNumber = smallest + 1 

            if nextNumber not in d: 
                return False 
            else: 
                smallest = nextNumber
        
        return len(d) == 0