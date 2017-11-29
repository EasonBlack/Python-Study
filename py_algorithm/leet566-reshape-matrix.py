class Solution(object):
    def matrixReshape(self, nums, r, c):
        nr = len(nums)
        if nr == 0 :
            return []
        nc = len(nums[0])
        if nc ==0:
            return [[]]
        # print nc * nr , r * c
        if nc * nr != r * c:
            return nums
        origin = []
        for i in range(len(nums)):
            origin = origin + nums[i]
        result = []
        for i in range(r):
            _r = origin[0:c]
            del origin[0:c]
            result.append(_r)
        return result


nums = [
    [1,2],
    [3,4]
]
print Solution().matrixReshape(nums, 2, 4)