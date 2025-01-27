# 可以用set，如果字母出現過的話，代表成對，len+2，並且移出set
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chr_set = set()
        length = 0

        for chr in s:
            if chr in chr_set:
                length += 2
                chr_set.remove(chr)
            else:
                chr_set.add(chr)
            
        if chr_set:
            length += 1

        return length
        
    
solution = Solution()
print(solution.longestPalindrome("abccccdd"))

                

