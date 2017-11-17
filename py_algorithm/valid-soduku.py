class Solution(object):
    def isValidSudoku(self, board):
      
      for i in range(0,9):
        col = set();line = set();cube = set()
        for j in range(0,9):
          if board[j][i]!='.' and board[j][i] in col:
            return False
          else:
            col.add(board[j][i])
          
          if board[i][j]!='.' and board[i][j] in line:
            return False
          else:
            line.add(board[i][j])

          if board[ 3*(i/3) + j/3][3*(i%3) + j%3]!='.' and board[ 3*(i/3) + j/3][3*(i%3) + j%3] in cube:
            return False
          else:
            cube.add(board[ 3*(i/3) + j/3][3*(i%3) + j%3])

      return True

    
    def solveSudoku(self, board):
      for i in xrange(9):
        for j in xrange(9):
          if board[i][j] == '.':
            for c in "123456789":
              if self.isValid(board, i , j ,c):
                board[i][j] = c
                print i , j , c
                if self.solveSudoku(board):
                  return True
                else:
                  board[i][j] = '.'    
            return False
      return True
    
    def isValid(self, board, row, col, c):
      for i in range(9):
        if  board[i][col] == c: return False
        if  board[row][i] == c: return False
        if  board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c:
          return False
      return True

list = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
list2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

print Solution().isValidSudoku(list)
print Solution().solveSudoku(list2)
print list2