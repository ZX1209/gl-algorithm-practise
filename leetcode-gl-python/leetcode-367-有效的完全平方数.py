# leetcode-367-有效的完全平方数.py
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

# 说明：不要使用任何内置的库函数，如  sqrt。

# 示例 1：

# 输入：16
# 输出：True
# 示例 2：

# 输入：14
# 输出：False

"""
思路:
就是逼近啊,,看看是不是

参考直接用sqrt了..虽说这都不是函数呢.
"""



class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False

        i = 1
        while i**2<num:
            i+=1

        return i**2==num