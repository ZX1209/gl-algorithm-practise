# leetcode-695-岛屿的最大面积.py
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

# 示例 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

# 示例 2:

# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。

# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。


"""
思路:
优化,迭代处理吗..
"""

from functools import lru_cache
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        rl = len(grid)
        cl = len(grid[0])

        def dfs(r,c):
            nonlocal grid,rl,cl,ans

            if 0<=r<rl and 0<=c<cl and grid[r][c]==1:
                grid[r][c] = 0
                return 1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c+1)+dfs(r,c-1)
            else:
                return 0

        for ri in range(rl):
            for ci in range(cl):
                if grid[ri][ci]==1:
                    ans = max(ans,dfs(ri,ci))
        return ans


执行用时为 96 ms 的范例
class Solution:
    def maxAreaOfIsland(self, grid):
        area = 0
        row = len(grid)
        if row > 0:
            col = len(grid[0])
            for r in range(row):
                for c in range(col):
                    if grid[r][c] == 1:
                        grid[r][c] = 0
                        a = [(c, r)]
                        i = 0
                        while i < len(a):
                            (x, y) = a[i]
                            if x > 0 and grid[y][x-1] == 1:
                                grid[y][x-1] = 0
                                a.append((x - 1, y))
                            if y > 0 and grid[y-1][x] == 1:
                                grid[y-1][x] = 0
                                a.append((x, y - 1))
                            if x + 1 < col and grid[y][x+1] == 1:
                                grid[y][x+1] = 0
                                a.append((x + 1, y))
                            if y + 1 < row and grid[y+1][x] == 1:
                                grid[y+1][x] = 0
                                a.append((x, y + 1))
                            i = i + 1
                        if len(a) > area:
                            area = len(a)
        return area
