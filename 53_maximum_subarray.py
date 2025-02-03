# Dynamic Programming

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]
        start = 0
        end = 0
        temp = 0
        for i in range(1, len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
                temp = i

            if current_sum > max_sum:
                max_sum = current_sum
                start = temp
                end = i
        return nums[start : end + 1]

                
                
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))