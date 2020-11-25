class Solution:
    
    def romanToInt(self, s: str) -> int:
        elem = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        oldNum = 0
        for i in range(len(s) - 1, -1, -1):
            current_num = elem[s[i]]
            if (current_num > oldNum):
                oldNum = current_num
                
            if (current_num < oldNum):
                number -= current_num
            else:
                number += current_num
        return number;
         
         
a = Solution()
s = input()
result = a.romanToInt(s)
print(result)
