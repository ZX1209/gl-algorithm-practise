# leetcode-400-第N个数字.py
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

# 注意:
# n 是正数且在32为整形范围内 ( n < 231)。

# 示例 1:

# 输入:
# 3

# 输出:
# 3
# 示例 2:

# 输入:
# 11

# 输出:
# 0

# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。


"""
思路:
1-9
10-19
100-199
...


重点在?

有点像多重循环呢..

果然是开始位和偏移位来算的,,但我推不出规律??

啊啊..解答即参考

没找对规律啊..

0,1,,,啊啊啊
"""

def nnums():
    for  i in range(1,100):
        for c in str(i):
            yield c

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        digits = 9

        while n>digits:
            n -= digits
            digits = (length+1)*9*(10**length)
            length+=1

        start = 10**(length-1) # int that start the dights mode
        num,digit = divmod(n-1,length)
        num += start

        return int(str(num)[digit])

# 参考 
# 执行用时为 20 ms 的范例
# class Solution(object):
#     def findNthDigit(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         digit=1
#         base=9
#         ith=1
#         while n>base*digit:
#             n=n-base*digit
#             digit=digit+1
#             ith=ith+base
#             base=base*10
#         return ord(str(ith+(n-1)/digit)[(n-1)%digit])-ord('0')