class Solution():
    def twoSum(self, nums, target):
      d = {}
      for index,num in enumerate(nums):
        t = target - num
        d[t] = index
      for index,num in enumerate(nums):
        if d.get(num):
          return [index, d[num]]


a = Solution()
b = a.twoSum([3,1,2,4], 6)
print b
