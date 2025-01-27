from collections import defaultdict
class Solution(object):
    # 這個最佳解用dict來解
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count = defaultdict(int)
        
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1

        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True
    

solution = Solution()
print(solution.isAnagram("apple", "elppa"))