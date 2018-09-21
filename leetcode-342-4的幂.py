# leetcode-342-4的幂.py
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

# 示例 1:

# 输入: 16
# 输出: true
# 示例 2:

# 输入: 5
# 输出: false
# 进阶：
# 你能不使用循环或者递归来完成本题吗？



"""
思路:
数字to2进制字符串喽


参考,,嗯,,有参考意义
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1:
            return False
        numstr = bin(num)

        return bool(len(numstr)%2 and numstr.count('1') == 1 and numstr[2]=='1')


# 参考 
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def isPowerOfFour(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num<=0:
#             return False
#         return 4**(int(math.log10(num)/math.log10(4)))==num