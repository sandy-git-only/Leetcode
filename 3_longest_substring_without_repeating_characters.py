class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chr_set = set()
        left = 0
        max_length = 0
        for i in range (len(s)):
            while s[i] in chr_set:
                chr_set.remove(s[left])
                left += 1            
            chr_set.add(s[i])
            max_length = max(max_length, i - left + 1)
        return max_length
    
solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))