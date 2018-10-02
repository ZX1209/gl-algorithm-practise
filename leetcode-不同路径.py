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

可以优化到不用深搜呢..
"""


class Solution(object):
    def dfs(self,r,c):
        if self.note[r][c]!=-1:
            return self.note[r][c]

        tmp = 0
        for dr,dc in ((1,0),(0,1)):
            if 0<=r+dr<self.rl and 0<=c+dc<self.cl:
                tmp += self.dfs(r+dr,c+dc)

        self.note[r][c] = tmp
        return self.note[r][c]


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<=0 or n<=0 :
            return 0 
        self.rl = n
        self.cl = m

        self.note = [[-1]*self.cl for j in range(self.rl)]
        self.note[self.rl-1][self.cl-1] = 1
        tmp = self.dfs(0,0)
        print(self.note)
        return tmp


执行用时为 20 ms 的范例
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        totalStep = m + n - 2
        minStep = min(m-1, n-1)
        fenzi = 1
        fenmu = 1
        for i in range(minStep, 0, -1):
            fenzi *= totalStep
            totalStep -= 1
            fenmu *= i
            a = fenzi
            b =fenmu
            while b!= 0:
                r = b
                b = a % b
                a = r
            fenzi = int(fenzi / a)
            fenmu = int(fenmu / a)
        return int(fenzi / fenmu)

执行用时为 24 ms 的范例
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        route = [[0]*m for _ in range(n)]
        route[0][0] = 1

        for i in range(n):
            for j in range(m):
                if i == 0 and j ==0:
                    continue
                if i == 0:
                    route[i][j]  = route[i][j-1]
                elif j==0:
                    route[i][j] = route[i-1][j]
                elif i - 1>=0 and j-1 >=0:
                    route[i][j] = route[i][j-1]+route[i-1][j]
        return route[n-1][m-1]