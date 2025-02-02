class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0] * (n+1)
        steps[0], steps[1], steps[2] = 0, 1, 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:    
            for i in range(3, n+1):
                steps[i] = steps[i-1] + steps[i-2]
            return steps[n]


solution = Solution()
print(solution.climbStairs(3))