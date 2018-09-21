# leetcode-371-两整数之和.py
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

# 示例 1:

# 输入: a = 1, b = 2
# 输出: 3
# 示例 2:

# 输入: a = -2, b = 3
# 输出: 1


"""
思路:
加法器..

不是很好理解呢..反码,补码之类的 
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        bu = 0
        if a<0 or b<0:
            bu = 1
        MASK = 0xffffffff
        MAX_INT = 0x7fffffff

        while b!=0:
            total = (a^b)&MASK
            carry = ((a&b)<<1) & MASK
            print(a,b,bin(a),bin(b),total,carry,bin(total),bin(carry))
            a,b = total,carry

        if a<0:
            a -= 1

        return a if a <MAX_INT else -(a^MASK)

if __name__ == '__main__':
    a,b = -12,-1
    test = Solution()
    r = test.getSum(a,b)
    print(r)



# 参考 
# 执行用时为 20 ms 的范例
# class Solution(object):
#     def getSum(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         MAX_INT = 0x7FFFFFFF
#         MASK = 0x100000000
#         r, c, p = 0, 0, 1
#         while a | b | c:
#             if (a ^ b ^ c) & 1: r = (r | p) % MASK
#             p <<= 1
#             c = (a & b | b & c | a & c) & 1
#             a = (a >> 1) % MASK
#             b = (b >> 1) % MASK
#         return r if r <= MAX_INT else ~((r & MAX_INT) ^ MAX_INT)