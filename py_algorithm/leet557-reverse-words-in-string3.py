class Solution(object):
    def reverseWords(self, s):
      
        return ' '.join( map(lambda x:x[::-1], s.split(' ')))


print Solution().reverseWords('Let\'s take LeetCode contest')