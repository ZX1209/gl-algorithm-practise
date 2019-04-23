# leetcode-441-排列硬币.py
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

# 给定一个数字 n，找出可形成完整阶梯行的总行数。

# n 是一个非负整数，并且在32位有符号整型的范围内。

# 示例 1:

# n = 5

# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤

# 因为第三行不完整，所以返回2.
# 示例 2:

# n = 8

# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# 因为第四行不完整，所以返回3.


"""
思路:
忘记可以用逆生成式了..真式的.
sn = n(a1+an)/2


"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        # def Sn(a1,an,n,d=None):
        #     if d!=None:
        #         n = 1 + (an-a1)/d
                
        #     return n*(a1+an)/2

        tmpsum = 0
        i = 1
        while True:
            if n<tmpsum+i:
                return i-1 
            else:
                tmpsum+=i
                i+=1


# (k+0.5)**2 - 0.25  =2*n
# 即 k**2+k = 2*n
# 即 等差求和公式
# 其中 k 为an,1为a1,n为Sn

执行用时为 36 ms 的范例
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = int((2*n+0.25)**0.5-0.5)
        return k