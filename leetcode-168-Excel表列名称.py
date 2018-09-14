# leetcode-168-Excel表列名称.py
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。

# 例如，

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# 示例 1:

# 输入: 1
# 输出: "A"
# 示例 2:

# 输入: 28
# 输出: "AB"
# 示例 3:

# 输入: 701
# 输出: "ZY"

"""
思路:
27进制..
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        i = 1
        ans = []

        while n:
            ans.append(chr(n%26+65))
            n = n//(27)**i
            i += 1

        return "".join(ans[::-1])