from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        right = 0

        dq = deque()

        while right < len(nums):

            # Remove smaller values
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add right pointer
            dq.append(right)

            # Move left if window is too big
            if right - left + 1 > k:
                left += 1

            # Remove indices that are outside the window
            if dq and dq[0] < left:
                dq.popleft()

            # Full window
            if right - left + 1 == k:
                res.append(nums[dq[0]])

            right += 1

        return res