class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map= {
            "V":5,
            "L":50,
            "D":500,
            "M":1000,
            "I":1,
            "X":10,
            "C":100
        }
        sum = 0
        for i in range(len(s)):
            if i > 0 and map[s[i-1]] < map [s[i]]:
                print( map[s[i]])
                sum += map[s[i]] - 2*map[s[i-1]] #因為前面已經加了一次，這邊要減回來
            else:
                sum += map[s[i]]

        return sum
solution = Solution()
print(solution.romanToInt("MCMXCIV"))