# leetcode-旋转图像.py
# 给定一个 n × n 的二维矩阵表示一个图像。

# 将图像顺时针旋转 90 度。

# 说明：

# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

# 示例 1:

# 给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:

# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 

# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

"""
思路:
一开始真是错的可以,,直接想要移一整行,,没有考虑到,,其实
移动有点过嗯

正确的应该是移动前面的三个就好了..

(最后的元素,,重复移动了....真是的..)

参考思想跟我差不多,,
但是,我确实做的有点麻烦欸..

"""


def rotate_out_side(matrix):
    l = len(matrix)-1
    base = 0
    while l>0:
        for i in range(l):
            row,col = 0,i
            prow,pcol = l - col,row
            print(row,col," ",prow,pcol)
            matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]

            row,col = prow,pcol
            prow,pcol = l - pcol,prow
            print(row,col," ",prow,pcol)
            matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]

            row,col = prow,pcol
            prow,pcol = l - pcol,prow
            print(row,col," ",prow,pcol)
            matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]

            # row,col = prow,pcol
            # prow,pcol = l - pcol,prow
            # matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]
        base +=1
        l -= 2
    return matrix


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)-1
        base = 0
        while l>0:
            for i in range(l):
                row,col = 0,i
                prow,pcol = l - col,row
                print(row,col," ",prow,pcol)
                matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]

                row,col = prow,pcol
                prow,pcol = l - pcol,prow
                print(row,col," ",prow,pcol)
                matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]

                row,col = prow,pcol
                prow,pcol = l - pcol,prow
                print(row,col," ",prow,pcol)
                matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]

                # row,col = prow,pcol
                # prow,pcol = l - pcol,prow
                # matrix[base+prow][base+pcol],matrix[base+row][base+col] = matrix[base+row][base+col],matrix[base+prow][base+pcol]
            base +=1
            l -= 2

# 参考
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         for i in range(n/2):
#             for j in range(i, n-1-i):
#                 temp = matrix[i][j]
#                 matrix[i][j] = matrix[n-1-j][i]
#                 matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
#                 matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
#                 matrix[j][n-1-i] = temp