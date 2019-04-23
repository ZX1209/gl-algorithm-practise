# leetcode-搜索二维矩阵-II.py
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例:

# 现有矩阵 matrix 如下：

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。

# 给定 target = 20，返回 false。


"""
思路:
提示太明显了吧...

一次没找到不代表就是错的啊...,,还是没有看清题目呢....

嗯,范例 想的挺明白的啊....
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rowl = len(matrix)
        if rowl <= 0:
            return False
        coll = len(matrix[0])
        if coll <= 0:
            return False
        i = 0
        j = 0
        while i<rowl:
            if matrix[i][0] <= target <= matrix[i][coll-1]:
                try:
                    matrix[i].index(target)
                    return True 
                except:
                    pass
            i+=1
        return False


执行用时为 56 ms 的范例
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n-1
        while row < m and col >= 0:
            temp = matrix[row][col]
            if temp == target:
                return True
            elif temp < target:
                row += 1
            else:
                col -= 1
        return False




if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    target = 5
    test = Solution()
    r = test.searchMatrix(matrix,target)
    print(r)