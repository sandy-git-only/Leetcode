class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = set() # 確保唯一組合
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1 #注意最後一個是index減一
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return list(output) 
        
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))