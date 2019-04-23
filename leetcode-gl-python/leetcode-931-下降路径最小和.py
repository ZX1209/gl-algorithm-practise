# leetcode-931-下降路径最小和.py
# 给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

# 下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

 

# 示例：

# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：12
# 解释：
# 可能的下降路径有：
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 和最小的下降路径是 [1,4,7]，所以答案是 12。

 

# 提示：

# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100


"""
思路:
dfs ??
"""

from functools import lru_cache

class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.l = len(A)

        @lru_cache(maxsize=None)
        def dfs(i,j):
            if j<0 or j>=self.l or i>=self.l:
                return float('inf')

            if i==self.l-1:
                return A[i][j]
            elif i<self.l:
                return A[i][j]+min(dfs(i+1,j),dfs(i+1,j+1),dfs(i+1,j-1))

        tmp = float('inf')
        for j in range(self.l):
            tmp = min(dfs(0,j),tmp)

        return int(tmp)

if __name__ == '__main__':
    A = [[51,24],[-50,82]]
    test = Solution()
    r = test.minFallingPathSum(A)
    print(r)

