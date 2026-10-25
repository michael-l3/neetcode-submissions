
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # will have to keep track of the smallest
        # will have to keep track of the largest as well
        maxProduct = max(nums)
        currL = 1
        currS = 1

        for number in nums:
            tempL = currL
            tempS = currS

            currL = max(tempL * number, tempS * number, number)
            currS = min(tempL * number, tempS * number, number)

            maxProduct = max(currL, maxProduct, number)

        return maxProduct
