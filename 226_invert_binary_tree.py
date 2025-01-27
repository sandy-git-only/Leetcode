# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return []
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)

        return root
    
solution = Solution()
print(Solution().invertTree([2,1,3]))