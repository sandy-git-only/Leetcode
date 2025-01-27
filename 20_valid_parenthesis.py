class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        
        stack = []
        for i in s:
            if i in par_map:
                stack.append(i)
            elif stack and i == par_map[stack[-1]]: #stack[-1]:  因為排序按順序所以後進先出
                stack.pop()
            else:
                return False
        return stack == []
       



solution = Solution()
print(solution.isValid("[()]"))