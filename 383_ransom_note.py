from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_table = defaultdict(int)
        for i in magazine:
                hash_table[i] += 1
        print(hash_table)

        for chr in ransomNote:
            if chr in hash_table:
                if hash_table[chr] >0 :
                    hash_table[chr] -= 1
                else:
                    return False
            else:
                 return False
        return True
        

solution = Solution()
print(solution.canConstruct("a", "b"))