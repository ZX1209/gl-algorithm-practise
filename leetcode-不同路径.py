# leetcode-不同路径.py
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 问总共有多少条不同的路径？



# 例如，上图是一个7 x 3 的网格。有多少可能的路径？

# 说明：m 和 n 的值均不超过 100。

# 示例 1:

# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:

# 输入: m = 7, n = 3
# 输出: 28


"""
思路:
感觉是数学题啊... 

先试试深搜吧
"""


class Solution(object):
    def dfs(self,r,c):
        if r==(self.rl-1) and c == (self.cl-1):
            self.ans += 1
            return None

        for dr,dc in ((-1,0),(0,1)):
            tmp = 0
            if 0<=r+dr<self.rl and 0<=c+dc<self.cl:
                tmp = self.dfs(r+dr,c+dc)


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.rl = n
        self.cl = m
        self.ans = 0
        self.note = [[-1]*cl]*rl

        self.dfs(0,0)

        return self.ans