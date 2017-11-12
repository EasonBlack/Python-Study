# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6


class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        maxNum = dp[0]
        for i in range(1, n):
            dp[i] = nums[i] + (dp[i - 1] if  dp[i - 1] > 0 else 0)
            maxNum = max(maxNum, dp[i])
        return maxNum

nums = [1]
print Solution().maxSubArray(nums)