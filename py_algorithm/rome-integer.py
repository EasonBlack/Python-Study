class Solution(object):
    def romanToInt(self, s):
        roman = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D" :500, "M":1000}
        s = s[::-1]
        n = len(s)
        step = 0
        result = 0
        prev = 0
        while step < n:
          current = roman[s[step]]
          result += current * (-1, 1)[current >= prev]
          prev = current
          step += 1
        return result
      
    def intToRoman2(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
    
    def intToRoman(self, num):
        roman = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D" :500, "M":1000}
        extra = {"": 0, "IV" : 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        sortedRoman = sorted(roman.items(), key=lambda value: value[1])
        sortedExtra =  sorted(extra.items(), key=lambda value: value[1])
        n = len(sortedRoman) - 1
        m = len(sortedExtra) - 1
        result = []
      
        while num > 0 and n >= 0:
          count = num // sortedRoman[n][1]
          if count > 0:    
            result.extend( [sortedRoman[n][0]] * count )
            num = num % sortedRoman[n][1]

          if num - sortedExtra[m][1] >= 0:
            result.append(sortedExtra[m][0])
            num = num - sortedExtra[m][1]
         

          n-=1
          m-=1
        return ''.join(result)

print Solution().romanToInt('DCXXI')
print Solution().intToRoman(399)
print Solution().intToRoman2(399)