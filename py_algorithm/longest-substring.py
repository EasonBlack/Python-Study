# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution(object):
  def lengthOfLongestSubstring(self, s):
    n = len(s)
    ans, i,j = 0, 0,0
    strAns = ''
    while (i < n and j < n) :
      if s[j] not in strAns:
        strAns = strAns + s[j]
        j+=1
        ans = max(ans, j - i)   
      else: 
        strAns = strAns[1:]
        i += 1 
    return ans

a = Solution()
print a.lengthOfLongestSubstring('abcabcdd')