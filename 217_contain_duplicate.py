class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_num = set(nums)
        if len(nums) == len(set_num):  
            return False
        else:
            return True

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))