# leetcode-479-最大回文数乘积.py
# 你需要找到由两个 n 位数的乘积组成的最大回文数。

# 由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。

# 示例:

# 输入: 2

# 输出: 987

# 解释: 99 x 91 = 9009, 9009 % 1337 = 987

# 说明:

# n 的取值范围为 [1,8]。

"""
思路:
数学题吧??

还是从大到小遍历呢..
"""

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 参考
        if n == 1:
            return 9

        for a in range(1,9*10**(n-1)):
            hi = (10**n)-a 
            lo = int(str(hi)[::-1])

            if a**2-4*lo<0:
                continue

            if (a**2-4*lo)**0.5 == int((a**2-4*lo)**0.5):
                return (lo + 10**n*(10**n-a))%1337


执行用时为 40 ms 的范例
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999][n - 1] % 1337