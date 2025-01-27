class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        orgColor = image[sr][sc]

        if orgColor == color:
            return image
        
        def dfs(row, col):
            # base case
            if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col]!= orgColor:
                return
            
            # upadate pixel color
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image


solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))