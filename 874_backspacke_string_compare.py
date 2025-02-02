class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def backspace(string):
            arr = []
            for i in string:
                if i == "#":
                        if len(arr) > 0:
                            arr.pop()
                        else:
                             pass
                else:
                    arr.append(i)
            return arr
        print(backspace(s))
        print(backspace(t))
        return backspace(s) == backspace(t)
    
solution = Solution()
print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))