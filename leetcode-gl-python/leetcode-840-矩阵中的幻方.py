# leetcode-840-矩阵中的幻方.py
# 3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

# 给定一个由整数组成的 N × N 矩阵，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。

 

# 示例 1:

# 输入: [[4,3,8,4],
#       [9,5,1,9],
#       [2,7,6,2]]
# 输出: 1
# 解释: 
# 下面的子矩阵是一个 3 x 3 的幻方：
# 438
# 951
# 276

# 而这一个不是：
# 384
# 519
# 762

# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 提示:

# 1 <= grid.length = grid[0].length <= 10
# 0 <= grid[i][j] <= 15

"""
思路:
幻方表
"""

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def matrixEqual(m1,m2):
            """假设两list都为3*3
            """
            for ri in range(3):
                for ci in range(3):
                    if m1[ri][ci]!=m2[ri][ci]:
                        return False

            return True
        magicMatrixs = [
            [[4,9,2],
            [3,5,7],
            [8,1,6]],

            [[2,9,4],
            [7,5,3],
            [6,1,8]],

            [[8,1,6],
            [3,5,7],
            [4,9,2]],

            [[6,1,8],
            [7,5,3],
            [2,9,4]],

            [[6,7,2],
            [1,5,9],
            [8,3,4]],

            [[8,3,4],
            [1,5,9],
            [6,7,2]],

            [[2,7,6],
            [9,5,1],
            [4,3,8]],

            [[4,3,8],
            [9,5,1],
            [2,7,6]]
        ]

        rl = len(grid)
        cl = len(grid[0])
        ans = 0

        for ri in range(rl-2):
            for ci in range(cl-2):
                tmpgrid = [r[ci:ci+3] for r in grid[ri:ri+3]]
                for magicMatrix in magicMatrixs:
                    if matrixEqual(tmpgrid,magicMatrix):
                        ans += 1
                        break
        return ans


执行用时为 44 ms 的范例
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(g):
            if sorted(g) != list(range(1, 10)):
                return False
            if sum(g[:3 ]) != 15 or sum(g[3: 6]) != 15 or sum(g[6:]) != 15:
                return False
            if g[0] + g[3] + g[6] != 15 or g[1] + g[4] + g[7] != 15 or g[2] + g[5] + g[8] != 15:
                return False
            return True
        count = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 5:
                    temp = []
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + 2):
                            temp.append(grid[a][b])
                    if isMagic(temp):
                        count += 1
        return count