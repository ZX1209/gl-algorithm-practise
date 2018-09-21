# leetcode-231-2的幂.py
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:

# 输入: 1
# 输出: true
# 解释: 20 = 1
# 示例 2:

# 输入: 16
# 输出: true
# 解释: 24 = 16
# 示例 3:

# 输入: 218
# 输出: false

"""
思路:
首先不能简单的除以2 呢..

但可以作为忧化点

参考,一直除,看看最后能不能除到1
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        return bin(n).count('1') == 1



# 参考
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         while n%2 == 0 and n>1:
#             n = n/2
#         return (n==1)