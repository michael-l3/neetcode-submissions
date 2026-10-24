class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        furthest = 0
        
        # We loop up to len(nums) - 2 because we don't need to jump *from* the final destination
        for i in range(len(nums) - 1):
            
            # Continuously scout the furthest reach from where we stand
            furthest = max(furthest, i + nums[i])
            
            # If we have reached the end of our current jump range...
            if i == current_end:
                jumps += 1              # We must take another jump!
                current_end = furthest   # Our new boundary becomes our furthest scouted horizon
                
        return jumps