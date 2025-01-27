from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = len(nums) // 2
        print(maj)
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
            print(num_map)
            if num_map[num] > maj:
                return num
            
solution = Solution()
print(solution.majorityElement([1,1,3,1,1,2,4]))