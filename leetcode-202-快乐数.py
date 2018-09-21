# leetcode-202-快乐数.py
# 编写一个算法来判断一个数是不是“快乐数”。

# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

# 示例: 

# 输入: 19
# 输出: true
# 解释: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


"""
思路:
嗯,,基本上,就是模拟下了..

循环会包含四??

啊啊啊啊


"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            if n == 1:
                return True

            if n == 4:
                return False

            n = sum([int(c)*int(c) for c in str(n)])


# 参考 
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         d = {}
#         while True:
#             m = 0
#             while n > 0:
#                 m += (n % 10)**2
#                 n = n // 10
#             if m in d:
#                 return False
#             if m == 1:
#                 return True
#             d[m] = m
#             n = m
