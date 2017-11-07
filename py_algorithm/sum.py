class Solution():
    def twoSum(self, nums, target):
      mirror= [target - val for val in nums if val != target-val ]
      result = [val for val in nums if val in mirror]
      return result


a = Solution()
b = a.twoSum([3,2,4,1,5], 6)
print b
