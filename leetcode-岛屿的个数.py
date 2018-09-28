# leetcode-岛屿的个数.py
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3


"""
思路:
我好像记得这道题呢..

闭包..
"""

class Solution(object):
    def dyeing(self,seedr,seedc):
        self.grid[seedr][seedc] = '2'
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0<=seedr+dr<self.rowl and  0<=seedc+dc<self.coll:
                if self.grid[seedr+dr][seedc+dc] == '1':
                    self.dyeing(seedr+dr,seedc+dc)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid

        self.rowl = len(grid)

        if self.rowl<=0:
            return 0

        self.coll = len(grid[0])

        

        ans = 0

        for i in range(self.rowl):
            for j in range(self.coll):
                if grid[i][j]=='1':
                    ans += 1
                    self.dyeing(i,j)

        return ans


# 执行用时为 64 ms 的范例
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if not grid:
#             return 0
#         count = 0
#         r = len(grid)
#         c = len(grid[0])
#         def helper(i,j):
#             grid[i][j] = "0"
#             if  j > 0 and grid[i][j-1] == "1":
#                 helper(i,j-1)
#             if j < c-1 and grid[i][j+1] == "1":
#                 helper(i,j+1)
#             if i > 0 and grid[i-1][j] == "1":
#                 helper(i-1,j)
#             if i < r-1 and grid[i+1][j] == "1":
#                 helper(i+1,j)

#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == "1":
#                     helper(i,j)
#                     count += 1
#         return count