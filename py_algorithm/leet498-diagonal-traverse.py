# coding=utf-8

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.


# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]

class Solution(object):
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0 : return []
        r = 0; c= 0; m=len(matrix); n = len(matrix[0]); lst = []
        for i in range(m*n):
            lst.append( matrix[r][c] )
            if (r+c)%2 == 0:
                if c ==n-1 : r+=1
                elif r==0: c+=1
                else: 
                    r-=1
                    c+=1
            else:
                if r==m-1: c+=1
                elif c==0: r+=1
                else:
                    r+=1
                    c-=1

        return lst




matrix =  [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print Solution().findDiagonalOrder(matrix)