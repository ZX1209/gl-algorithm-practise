# leetcode-633-平方数之和.py
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

# 示例1:

# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
 

# 示例2:

# 输入: 3
# 输出: False

"""
思路:
明明是有abc都有个公式联系了,但还是疏忽了呢..真是的..

low high..
"""


from math import sqrt
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        # 参考
        a = 0

        while a <= sqrt(c/2):
            b = sqrt(c-a**2)
            if int(b) == b:
                return True
            a+=1
        return False

执行用时为 96 ms 的范例
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # import math
        # if c < 0:
        #     return False
        # e = int(math.sqrt(c) + 1)
        # s = 0
        # while s <= e:
        #     if s * s + e * e == c:
        #         return True
        #     elif c > s * s + e * e:
        #         s += 1
        #     else:
        #         e -= 1
        i=2
        while i**2<=c:
            count = 0
            if c%i ==0:
                while c%i ==0:
                    count+=1
                    c/=i
                if i%4 ==3 and count%2!=0:
                    return False
            i+=1
        return c%4!=3


if __name__ == '__main__':
    solution = Solution()
    solution.judgeSquareSum(5)


执行用时为 152 ms 的范例
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low = 0
        high = int(pow(c, 0.5))
        while low <= high:
            value = low*low+high*high
            if value < c:
                low += 1
            elif value > c:
                high -= 1
            else:
                return True
        return False