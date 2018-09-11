# leetcode-颠倒二进制位.py
# 颠倒给定的 32 位无符号整数的二进制位。

# 示例:

# 输入: 43261596
# 输出: 964176192
# 解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
#      返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？

"""
思路:
int('bin str',base=2)
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rn = bin(n)[-1:1:-1]
        rn = rn + '0'*(32-len(rn))
        return int(rn,2)

if __name__ == '__main__':
    n = 43261596
    test = Solution()
    r = test.reverseBits(n)
    print(r)



# 参考
# 执行用时为 24 ms 的范例
# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         return int(bin(n)[2:][::-1]+'0'*(32-len(bin(n)[2:])),2)