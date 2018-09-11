# leetcode-有效的数独.py
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


# 上图是一个部分填充的有效的数独。

# 数独部分空格内已填入了数字，空白格用 '.' 表示。

# 示例 1:

# 输入:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
# 示例 2:

# 输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
#      但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
# 说明:

# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 给定数独序列只包含数字 1-9 和字符 '.' 。
# 给定数独永远是 9x9 形式的。

"""
思路:
重复检测
与
区域划分
字符到数字的转换
"""

from collections import product

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        grid = [set() for i in range(9)]

        # for r,c in product(range(9),repeat=2):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = int(int(r / 3) * 3 + c / 3)
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])

        return True



# 参考-不行
# class Solution:
#     # @param board, a 9x9 2D array
#     # @return a boolean
#     def isValidSudoku(self, board):
#         row = [set([]) for i in range(9)]
#         col = [set([]) for i in range(9)]
#         grid = [set([]) for i in range(9)]

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     continue
#                 if board[r][c] in row[r]:
#                     return False
#                 if board[r][c] in col[c]:
#                     return False

#                 g = r / 3 * 3 + c / 3
#                 if board[r][c] in grid[g]:
#                     return False
#                 grid[g].add(board[r][c])
#                 row[r].add(board[r][c])
#                 col[c].add(board[r][c])

#         return True