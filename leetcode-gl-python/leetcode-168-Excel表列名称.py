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
不,是26进制,,原数全减1,,方便配对..(A~Z)..
我尽然没敢做呢..
"""

from collections import deque
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        column  = deque()

        while n>0:
            n,output = divmod(n-1,26)
            column.appendleft(output)

        return "".join([chr(i+ord('A')) for i in column])

        # i = 1
        # ans = []

        # while n:
        #     ans.append(chr(n%26+65))
        #     n = n//(26)**i
        #     i += 1

        # return "".join(ans[::-1])