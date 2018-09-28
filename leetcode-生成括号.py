# leetcode-生成括号.py
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


"""
思路:
所有括号组合,有2**n 个

有效的是说,,')'的个数要小于等于前面'('的个数??

一半一半吗?

rotate:
((( -> )))
(() -> ))(

reverse:
((( -> (((
(() -> )((

reverse,rote:
pass

l,r 吗..可以..


"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<=0:
            return []

        halfans = []
        ans = []

        def dfs(tstr,i):
            if i<=0:
                halfans.append(tstr)
            else:
                dfs(tstr+'(',i-1)
                if tstr.count('(')>tstr.count(')'): dfs(tstr+')',i-1)

        def reverse(tstr):
            tmpstr = ""
            for c in tstr:
                if c=='(':
                    tmpstr+=')'
                if c==')':
                    tmpstr+='('

            return tmpstr

        # 本来就有一个了..
        dfs("(",n-1)

        for left in halfans:
            for right in halfans:
                if right.count('(') == left.count('('):
                    ans.append(left+reverse(right[::-1]))

        return ans



# 执行用时为 24 ms 的范例
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         ans = []
#         def dfs(l, r, path):
#             if l:
#                 dfs(l-1, r, path + '(')
#             if r > l:
#                 dfs(l, r-1, path + ')')
#             if not r:
#                 ans.append(path)
#         dfs(n-1, n , '(')
#         return ans