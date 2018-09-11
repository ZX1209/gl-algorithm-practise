# leetcode-加一.py
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

"""
思路:
从后往前??

优化,,抢先停止
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)

        i = l-1
        digits[-1]+=1

        while i>0:
            if digits[i]>=10:
                digits[i]-=10
                digits[i-1]+=1
            i-=1

        if digits[0]>=10:
            digits[0]-=10
            digits.insert(0,1)

        return digits


# 参考
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         if digits == [] or digits == None:
#             return []
        
#         m = 1
#         n = len(digits) - 1
#         while n >= 0:
#             k = digits[n] + m
#             m = k // 10 
#             digits[n] = k % 10

#             if m == 0 and n > 0:
#                 return digits

#             n -= 1

#         if m != 0:
#             digits = [1] + digits 
#         return digits