point = 331
def guess(num):
  if num<point : 
    return -1
  elif num > point:
    return 1
  else: return 0

class Solution(object):
    def guessNumber(self, n): 
      low = 1
      high = n
      while low <= high :
          mid = low + (high - low) / 2
          res = guess(mid)
          if res == 0:
              return mid
          elif res < 0:
              low = mid + 1
          else:
              high = mid - 1
      
      return -1
 
  
print Solution().guessNumber(4100)