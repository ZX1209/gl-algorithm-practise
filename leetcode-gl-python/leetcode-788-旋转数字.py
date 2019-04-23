# leetcode-788-旋转数字.py
# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

# 示例:
# 输入: 10
# 输出: 4
# 解释: 
# 在[1, 10]中有四个好数： 2, 5, 6, 9。
# 注意 1 和 10 不是好数, 因为他们在旋转之后不变。
# 注意:

# N 的取值范围是 [1, 10000]。

"""
思路:
范例??
"""


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def splitNum(n):
            ans = []
            while n>0:
                ans.append(n%10)
                n//=10
            return ans

        def isViald(n):
            isunique = 0
            for nn in splitNum(n):
                if nn in {3,4,7}:
                    return False
                if nn not in {0,1,8}:
                    isunique = 1

            if isunique:
                return True
            else:
                return False

        ans = 0

        for i in range(1,N+1):
            if isViald(i):
                ans += 1

        return ans


执行用时为 40 ms 的范例
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d_self = [0]
        d_diff = [0]
        for i in range(10):
            d_self.append(d_self[-1])
            d_diff.append(d_diff[-1])
            if i in [0, 1, 8]:
                d_self[-1] += 1
            elif i in [2, 5, 6, 9]:
                d_diff[-1] += 1
            
        cur_diff, cur_all = 0, 1
        b = 0
        while N > 0:
            prev_diff, prev_all = cur_diff, cur_all
            r = N % 10
            total = pow(7,b)
            cur_all = (d_diff[r] + d_self[r]) * total
            cur_diff = cur_all - d_self[r] * pow(3,b)
            if r in [0, 1, 8]:
                cur_diff += prev_diff
                cur_all += prev_all
            elif r in [2, 5, 6, 9]:
                cur_diff += prev_all
                cur_all += prev_all
            N //= 10
            b += 1
        return cur_diff
