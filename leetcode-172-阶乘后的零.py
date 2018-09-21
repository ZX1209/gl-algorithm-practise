# leetcode-172-阶乘后的零.py
# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 示例 1:

# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 示例 2:

# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。

"""
思路:

找规律大法好..


参考是python2 写的吧..
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        tmp = 0

        while n>0:
            tmp+=n//5
            n = n//5
        return tmp

        # if n<=24:
        #     return n//5
        # else:
        #     return n//5+1


# 参考
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def trailingZeroes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         res = 0
#         while n > 0:
#             n = n/5
#             res += n
#         return res