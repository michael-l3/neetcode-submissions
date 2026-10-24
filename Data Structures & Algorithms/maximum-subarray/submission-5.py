class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = max(nums)
        currSub = nums[0]

        for number in nums[1:]: 
            currSub = max(currSub + number, number)
            maxSub = max(currSub,maxSub)

        return maxSub