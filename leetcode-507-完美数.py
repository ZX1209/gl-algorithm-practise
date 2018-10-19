# leetcode-507-完美数.py
# 对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

# 给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False

 

# 示例：

# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14
 

# 注意:

# 输入的数字 n 不会超过 100,000,000. (1e8)


"""
思路:
分解因子.
""" 
from math import sqrt

def Factorization(n):
    res = []
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            res.append(i)
            res.append(n//i)
    return res


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False

        tmp = Factorization(num)
        tmp = [i for i in tmp if i!=num]
        
        return sum(tmp) == num



执行用时为 40 ms 的范例
class Solution:
    def checkPerfectNumber(self, num):
        if num not in[6,28,496,8128,33550336,8589869056,137438691328]:
            return False
        else:
            return True

执行用时为 44 ms 的范例
class Solution:
    def checkPerfectNumber(self, num):
        ans = 1
        if num%2 != 0:
            return False
        for i in range(1, num):
            if num%(2**i) == 0:
                ans += 2**i
                if ans == num/(2**i):
                    return True
            if num < 2**i:
                return False
        return False