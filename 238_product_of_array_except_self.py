class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = nums[0]
        if len(nums) < 2:
            return []
        products = [0] * len(nums)
        for j in range(len(nums)):
            for i in range(0,len(nums), 2):
                product = nums[i+1] * nums[i+2]
                product
                print(product)
            products[j] = product
        return products
    
solution = Solution()
result = solution.productExceptSelf([1,2,3,4])
print(result)