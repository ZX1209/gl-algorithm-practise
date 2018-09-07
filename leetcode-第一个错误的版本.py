# leetcode-第一个错误的版本.py
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

# 示例:

# 给定 n = 5，并且 version = 4 是第一个错误的版本。

# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5) -> true
# 调用 isBadVersion(4) -> true

# 所以，4 是第一个错误的版本。


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool isbad
# def isBadVersion(version):

class Solution:
    def binaryFind(self, l, i, j):
        pass

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        if n==1:
            return 1

        i = 1
        j = n
        c = int(n/2)

        while i<j-1:
            # is bad
            if isBadVersion(c):
                j = c
                c = int((i+j)/2)
            # is good
            else:
                i = c
                c = int((i+j)/2)

        return i if isBadVersion(i) else j


# 参考
# 执行用时为 40 ms 的范例
# # The isBadVersion API is already defined for you.
# # @param version, an integer
# # @return a bool
# # def isBadVersion(version):

# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n<=0:return 0
#         if n==1:return 1
#         l = 1
#         r = n
#         while l < r:
#             m = int((l + r)/2)
#             if isBadVersion(m):
#                 r = m #因为在这里不是m-1因此有可能变成无限循环
#             else:
#                 l = m + 1
#         return r 