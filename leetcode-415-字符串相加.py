# leetcode-415-字符串相加.py
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

# 注意：

# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

"""
思路:
直接,,构造一个加下


范例,,作弊呢
"""



class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        l1 = len(num1)-1
        l2 = len(num2)-1
        ans = ""
        carry = 0
        tmp = 0

        while l1>=0 or l2 >=0 or carry:
            tmp = 0

            if carry:
                tmp+=1

            carry = 0

            if l1>=0:
                tmp += ord(num1[l1])-48
                l1 -= 1

            if l2>=0:
                tmp += ord(num2[l2])-48
                l2 -= 1

            if tmp>=10:
                tmp -= 10
                carry = 1

            ans = chr(tmp+48)+ans

        return ans

# 执行用时为 28 ms 的范例
# class Solution(object):
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         value1 = int(num1)
#         value2 = int(num2)
#         return str(value1 + value2)