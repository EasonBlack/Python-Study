# Given a 32-bit signed integer, reverse digits of an integer.
# 321 -> 123
# 1231231231341234123412341243 -> 0
# -120 - > -21


class Solution1(object):
  def reverse(self, x):
    sign =  (1, -1)[x < 0]
    strNum = str(abs(x))
    count = strNum.__len__()
    resultArr = []
    for i in range(count):
      resultArr.append(strNum[count - i - 1])
    intNum = int(''.join(resultArr))
    if intNum > 0x7fffffff:
      return 0
    else:
      return intNum * sign

class Solution(object):
  def reverse(self, x):
    sign =  (1, -1)[x < 0]
    x = abs(x)
    res = 0
    while x!=0:
      res = res * 10 +  x % 10
      x = x // 10
    return res * sign
  


a = Solution()
print a.reverse(-123)


