# leetcode-70-爬楼梯.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

"""
思路:
主要是时间限制吗?

"""

class Solution:
    def __init__(self):
        self.ans = 0
        self.d = {0:0,1:1,2:2,3:3,4:5,5:8,6:13,10:89}


    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <0:
            return 0

        if n in self.d:
            return self.d[n]

        self.d[n-1] = self.climbStairs(n-1)
        self.d[n-2] = self.climbStairs(n-2)

        return self.d[n-1] + self.d[n-2]



# 执行用时为 32 ms 的范例
# class Solution:
#     global f
#     f = collections.defaultdict(int)
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n < 0:
#             return 0
#         if n == 0:
#             return 1
#         if n in f.keys():
#             return f[n]
#         one_steps = self.climbStairs(n-1)
#         two_steps = self.climbStairs(n-2)
#         f[n] = one_steps + two_steps
#         return f[n]
