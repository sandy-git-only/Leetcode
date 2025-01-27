class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits_1(self, n):
        ans = 0
        for i in range(32):
            if n & 1: #(&:2元運算子)
                ans = ans + 2**(31-i)
            n = n >> 1

        return ans
    
    def reverseBits_2(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res << 1 # Shift left
            res += (n & 1) # Add the least significant bit of n to res
            n = n >> 1     # Shift n to the right
        return res   
        
        

solution = Solution()
print(solution.reverseBits_1(10111111111111111111111111111111))
print(solution.reverseBits_2(10111111111111111111111111111111))