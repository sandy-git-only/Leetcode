# # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #DFS
        if not root:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        return 1 + max(right, left) #1是因為要把自身的節點考慮進來，避免結果為0
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(None)
root.right.right = TreeNode(None)
solution = Solution()
print(solution.maxDepth(root))