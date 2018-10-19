# leetcode-504-七进制数.py
# 给定一个整数，将其转化为7进制，并以字符串形式输出。

# 示例 1:

# 输入: 100
# 输出: "202"
# 示例 2:

# 输入: -7
# 输出: "-10"
# 注意: 输入范围是 [-1e7, 1e7] 。


"""
思路:
范例也差不多啊
"""

def decToN(i,base):
    if i==0:
        return "0"
    ans = []
    flag = 0

    if i<0:
        flag = 1
        i = abs(i)

    while i>0:
        ans.append(str(i%base))
        i//=7

    if flag:
        ans.append('-')
    ans.reverse()

    return "".join(ans)

# 累比转换为二进制




class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        return decToN(num,7)


执行用时为 40 ms 的范例
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        np = '-' if num < 0 else ''
        num = abs(num)
        while num:
            res.append(num % 7)
            num //= 7
        if res == []:
            return '0'
        else:
            return np + ''.join(map(str, res[::-1]))
        