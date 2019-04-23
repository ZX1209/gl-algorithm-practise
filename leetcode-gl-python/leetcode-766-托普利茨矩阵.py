# leetcode-766-托普利茨矩阵.py
# 如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

# 给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

# 示例 1:

# 输入: 
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# 输出: True
# 解释:
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是True。
# 示例 2:

# 输入:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# 输出: False
# 解释: 
# 对角线"[1, 2]"上的元素不同。
# 说明:

#  matrix 是一个包含整数的二维数组。
# matrix 的行数和列数均在 [1, 20]范围内。
# matrix[i][j] 包含的整数在 [0, 99]范围内。
# 进阶:

# 如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？
# 如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？



class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """


        rl = len(matrix)
        cl = len(matrix[0])

        def isDsame(r,c):
            nonlocal matrix,cl,rl
            tmp = matrix[r][c]
            while r<rl and c<cl:
                if matrix[r][c] != tmp:
                    return False
                r+=1
                c+=1
            return True

        for ci in range(1,cl-1):
            if not isDsame(0,ci):
                return False

        for ri in range(rl-1):
            if not isDsame(ri,0):
                return False

        return True


执行用时为 52 ms 的范例
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0])
        i = 0   
        j = 0
        while(i+1<rows):
            # 按行遍历
            while(j+1<columns):
                # 按列遍历
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                j += 1
            j = 0
            i += 1
        return True