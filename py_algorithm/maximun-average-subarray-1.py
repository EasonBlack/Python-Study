# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.


class Solution(object):
    def findMaxAverage(self, nums, k):
             
        avg = 0
      
        for i in range(k):
            avg += nums[i]/float(k)
            
        maxnum = avg
        
        if len(nums) - k <=0:
            return avg
         
        for i in range(k, len(nums)):
            avg = avg - nums[i-k]/float(k) + nums[i]/float(k)
            maxnum = max(maxnum, avg)
          
        return maxnum


print Solution().findMaxAverage([4,2,1,3,3], 2)