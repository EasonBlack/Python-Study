class Solution(object):
    def findTheDifference(self, s, t):
      low = 0
      high = len(s)
      while  high-low > 1:
        mid = low + (high - low)/2
        # print low,mid,high, s[low:mid], s[mid:high]

        if s[low:mid] != t[low:mid]:
          high = mid    
        elif s[mid:high] != t[mid:high]:
          low = mid
        else:
          return t[-1]
      
      return t[low]

    def findTheDifference2(self, s, t):
      return [i for i in t if i not in s or s.count(i)!=t.count(i)][0]

print Solution().findTheDifference('abcdefg','pabcdefg')
print Solution().findTheDifference2('abcdefg','pabcdefg')