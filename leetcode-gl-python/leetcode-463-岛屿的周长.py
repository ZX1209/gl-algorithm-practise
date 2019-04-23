# leetcode-463-岛屿的周长.py
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

# 示例 :

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# 答案: 16
# 解释: 它的周长是下面图片中的 16 个黄色的边：

"""
思路:
四面推进? (4*n**2)

格子推导 需要特殊关系. 

递归计算? 

范例
这种
半 总体补全..
比较难证明呢..
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 参考
        rl,cl = len(grid),len(grid[0])

        for row in grid:
            row.append(0)

        grid.append([0]*(cl+1))

        permiter = 0

        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == 1:
                    permiter+=4
                    if grid[r][c+1]==1:
                        permiter-=2
                    if grid[r+1][c]==1:
                        permiter-=2
        return permiter




        # # where to search
        # rl = len(grid)
        # cl = len(grid[0])

        # ri = 0
        # ci = 0

        # for nr,nc,steps in ((0,1,cl),(1,0,rl),(0,-1,cl),(-1,0,rl)):
        #     # 处理
        #     for step in range(steps-1):
        #         ri+=nr
        #         ci+=nc
        #         print(ri,ci)


        # how to search
        #for dr,dc in ((1,0),(0,-1),(-1,0),(0,1))
        

执行用时为 148 ms 的范例
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter