# leetcode-2-两数相除.py
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 示例 1:

# 输入: dividend = 10, divisor = 3
# 输出: 3
# 示例 2:

# 输入: dividend = 7, divisor = -3
# 输出: -2
# 说明:

# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

"""
思路:
这,连续减?

进位乘?

二进制乘法?

结果溢出??
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isminus = 0

        if dividend<0:
            dividend = abs(dividend)
            isminus = 1 - isminus

        if divisor<0:
            divisor = abs(divisor)
            isminus = 1 - isminus



        dis  = len(bin(dividend)) - len(bin(divisor))
        if dis<0:
            return 0
        ans = []

        while dis>=0:
            tmp = dividend - (divisor<<dis)
            if tmp<0:
                ans.append("0")
                dis-=1
            elif tmp==0:
                ans.append("1")
                ans.append("0"*dis)
                break
            else:
                ans.append("1")
                dividend -= (divisor<<dis)
                dis-=1
        tmpans = int("".join(ans),2) if not isminus else -int("".join(ans),2)

        return tmpans if -2147483648<=tmpans<=2147483647 else 2147483647


执行用时为 52 ms 的范例
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res1= int(abs(dividend)/abs(divisor))
        if (dividend>0 and divisor<0 ) or (dividend<0 and divisor>0):
            res1*=-1
        if res1 > 2**31- 1 or res1 < -2**31:

            return 2**31-1
        else:
            return res1