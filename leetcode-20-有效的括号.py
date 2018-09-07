# leetcode-20-有效的括号.py


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {
            '(': ')',
            '[': ']',
            '{': '}',
            ')': '',
            ']': '',
            '}': ''
        }

        stack = []
        for single_s in s:
            if stack == []:
                stack.append(single_s)
            else:
                if match[stack[-1]] == single_s:
                    stack.pop()
                else:
                	stack.append(single_s)

        return stack == []


# 执行用时为 36 ms 的范例
# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         l=[]
#         dic={")":"(","]":"[","}":"{"}
#         for x in s:
#             if x in dic.values():
#                 l.append(x)
#             elif x in dic.keys():
#                 if l==[] or dic[x]!=l.pop():
#                     return False
#             else:
#                 return False
#         return l==[]