# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root:TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxDiameter = 0
        self.calDiameter(root)
        return self.maxDiameter
    
    def calDiameter(self, root):
        if not root:
            return 0
        left_path = self.calDiameter(root.left)
        right_path = self.calDiameter(root.right)
        
        currentDiameter = left_path + right_path
        self.maxDiameter = max(self.maxDiameter, currentDiameter)

        return max(left_path, right_path) + 1
        
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
solution = Solution()
print(solution.diameterOfBinaryTree(root))