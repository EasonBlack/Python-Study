# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution(object):
    def searchMatrixBetter(self, matrix, target):
      if not matrix or  not matrix[0]:
          return False
      col = len(matrix[0]) - 1
      row = 0
      while col >= 0 and row < len(matrix):
        current = matrix[row][col]
        if target == current:
          return True
        elif target > current:
          row += 1
        elif target < current:
          col -= 1
      return False

    def searchMatrix(self, matrix, target):
        
        if not matrix or  not matrix[0]:
          return False
      
        cols = [target - val[0] for val in matrix if target - val[0] >= 0]
        if not cols:
          return False  
        minIndex, colsMin = min(enumerate(cols), key=lambda v: v[1])
   
        result = False
        while minIndex >= 0:
          current = matrix[minIndex]
          minIndex-=1
          try:
            current.index(target)
            result = True
            break
          except:
            continue

        return result
        # current = matrix[minIndex] #if colsMin!=0 else matrix[minIndex] 
      
        
        


matrix = [
 
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print Solution().searchMatrix(matrix, 5)
print Solution().searchMatrixBetter(matrix, 5)