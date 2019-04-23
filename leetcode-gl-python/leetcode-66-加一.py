# leetcode-66-加一.py
# 题目描述提示帮助提交记录社区讨论阅读解答
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
嗯,,进位是吧..
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] += 1
        if digits[-1]<10:
            return digits

        l = len(digits)
        # 先信任之后各位有效
        for i in range(l - 1, 0, -1):
            if digits[i] >= 10:
                digits[i - 1] += 1
                digits[i] -= 10
            else:
                break

        if digits[0]>=10:
            digits[0] -= 10
            digits.insert(0,1)

        return digits


# 参考
# 执行用时为 36 ms 的范例
# class Solution:
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """ 
#         result=[]
#         if digits[-1]!=9:
#             digits[-1]=digits[-1]+1
#             result=digits
#         else:
#             num=0
#             digits.reverse()
#             for i in range(len(digits)):
#                 num=num+digits[i]*(10**(i))
#             num=str(num+1)
#             for j in num:
#                 result.append(int(j))
#         return result
