# leetcode-69-x的平方根.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:

# 输入: 4
# 输出: 2
# 示例 2:

# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。

"""
思路:
偷懒的话,直接用内置的喽..

"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**(1/2))


# 参考
# 执行用时为 52 ms 的范例
# class Solution:
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         r = x
#         while r * r > x:
#             r = (r + x // r) // 2
#         return r