class Solution(object):
    def triangleNumber(self, nums): 
        nums = [val for val in nums if val!=0]
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            k = i + 2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k+=1
                count += k - j -1
        
        return count

print Solution().triangleNumber([0, 2,3,4,6,7,1,3,4])