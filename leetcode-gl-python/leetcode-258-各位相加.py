# leetcode-258-各位相加.py
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

# 示例:

# 输入: 38
# 输出: 2 
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。


def int2list(num):
    tmpl = []
    while num:
        tmpl.append(num%10)
        num //= 10
    return tmpl

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numl = int2list(num)

        while len(numl) >1:
            tmpi = sum(numl)
            numl = int2list(tmpi)

        return numl


# 找规律
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        ans = num%9

        if ans:
            return ans
        else:
            return 9


# 参考 
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         if num >= 10:
#             if num % 9 ==0 and num !=0:
#                 return 9
#             else:
#                 return num%9
#         else:
#             return num