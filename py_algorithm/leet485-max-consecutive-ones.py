class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        dp = [0]*(len(nums) + 1)
        maxnum = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                dp[i] = dp[i+1] + 1
            maxnum =max(maxnum, dp[i])
        return maxnum

        # better way
        # return len(max(''.join(map(str, nums)).split('0')))

print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1])