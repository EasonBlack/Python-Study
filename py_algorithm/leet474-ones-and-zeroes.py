class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]
        for str in strs:
            numZeroes = str.count('0')
            numOnes = str.count('1')
            for x in range(m, numZeroes-1, -1):
                for y in range(n, numOnes-1, -1):
                    print x,y, '|' ,x-numZeroes,y-numOnes, '|' ,dp[x-numZeroes][y-numOnes], dp[x][y]
                    dp[x][y] = max(1 + dp[x-numZeroes][y-numOnes], dp[x][y])
                    # print x,y,'|' , x-numZeroes,y-numOnes, '|' , dp[x-numZeroes][y-numOnes], dp[x][y]
                print 'y loop stop'
            print 'x loop stop'
        return dp[m][n]

strs = ["10", "0001", "111001", "1", "0"]
print Solution().findMaxForm(strs, 5, 3)