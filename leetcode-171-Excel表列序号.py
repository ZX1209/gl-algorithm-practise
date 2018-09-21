# leetcode-171-Excel表列序号.py
# 给定一个Excel表格中的列名称，返回其相应的列序号。

# 例如，

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:

# 输入: "A"
# 输出: 1
# 示例 2:

# 输入: "AB"
# 输出: 28
# 示例 3:

# 输入: "ZY"
# 输出: 701


"""
思路:
这,又是一个进制转换呢..

从后往前,,从前往后(时间积累)
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = l-1
        ans = 0

        while i >= 0:
            ans += ((ord(s[i])-65)+1)*(26**(l-i-1))

            i -= 1

        return ans


# 参考 
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def titleToNumber(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         res = 0
#         base = ord('A') - 1
#         for c in s:
#             res = res * 26 + ord(c) - base
#         return res