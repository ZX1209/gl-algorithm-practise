# leetcode-矩阵置零.py
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

# 示例 1:

# 输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:

# 输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:

# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？


"""
思路:
记录0位置
集合
开刷


嗯 参考跟我差不多呢..
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowset = set()
        colset = set()

        rl = len(matrix)
        cl = len(matrix[0])

        for r in range(rl):
            for c in range(cl):
                if matrix[r][c] == 0:
                    rowset.add(r)
                    colset.add(c)


        for tr in rowset:
            matrix[tr][:] = [0]*cl

    
        for r in range(rl):
            for tc in colset:
                matrix[r][tc] = 0





# 参考 
# 执行用时为 104 ms 的范例
# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         zero = []
#         m = len(matrix)
#         n = len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     zero.append([i, j])
#         for pair in zero:
#             i = pair[0]
#             j = pair[1]
#             for k in range(m):
#                 matrix[k][j] = 0
#             for k in range(n):
#                 matrix[i][k] = 0