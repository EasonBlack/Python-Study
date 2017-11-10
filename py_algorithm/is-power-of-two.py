class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1 :
            return True
        if n == 0: return False

        while n !=1:
            if n % 2:
                return False          
            n = n / 2

        return True

    def isPowerOfTwo1(self, n):
        if n==0 : return False
        while n % 2 == 0:
            n = n/2
        return (n==1)
    
    def isPowerOfTwo2(self, n):
        if n ==0 : return False
        if n ==1 : return True
        if n % 2 ==0: return self.isPowerOfTwo2(n/2) 
        else: return False
        
n = 2046
print Solution().isPowerOfTwo(n)
print Solution().isPowerOfTwo1(n)
print Solution().isPowerOfTwo2(n)
        