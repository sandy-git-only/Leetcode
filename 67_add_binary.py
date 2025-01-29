class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_ab = int(a, 2) + int(b, 2)
        binary = ""

        if sum_ab == 0:
            return 0
        
        while sum_ab > 0:
            binary = str(sum_ab % 2) + binary # Not binary += .... (wrong order)
            sum_ab //= 2
        return binary
    
solution = Solution()
print(solution.addBinary("11", "1"))