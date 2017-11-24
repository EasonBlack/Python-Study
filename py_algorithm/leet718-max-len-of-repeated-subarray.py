class Solution(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)
      
# A = [16,33,14,2,98]; B=[55,24,97,50,38]
# A = [70,39,25,40,7]; B=[52,20,67,5,31]
A = [0,0,0,0,1];B = [1,0,0,0,0]
# A = [1,0,0,0,1];B = [1,0,0,1,1]
# A = [1,2,3,2,1];B = [3,2,1,4,7]

print Solution().findLength(A,B)