# leetcode-693-交替位二进制数.py
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。

# 示例 1:

# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
# 示例 2:

# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
# 示例 3:

# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
#  示例 4:

# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010



"""
思路:
in..操作
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]
        l = len(b)

        i = 0
        while i<l-1:
            if b[i]==b[i+1]:
                return False
            i+=1
        return True   


执行用时为 36 ms 的范例
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        string = bin(n)[2:]
        odd = string[1::2]
        even = string[::2]
        if ('1' in even and '1' in odd) or ('0' in even and '0' in odd):
            return False
        return True
        