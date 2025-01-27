# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root:TreeNode):
        if not root:
             return 0
        l_dep = self.maxDepth(root.left)
        if l_dep == -1:
            return -1
        r_dep = self.maxDepth(root.right)
        if r_dep == -1 :
            return -1
        
        if abs(l_dep - r_dep) > 1:
            return -1
        
        return max(l_dep, r_dep) + 1
        
    def isBalanced(self, root:TreeNode):
        return self.maxDepth(root) != -1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.isBalanced(root))
