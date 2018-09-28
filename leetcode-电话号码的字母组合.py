# leetcode-电话号码的字母组合.py
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



# 示例:

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

"""
思路:
不知为何范例比我快??算了,,思路都一样.;.

回溯,,深搜把..
"""



class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz"
        }
        l = len(digits)
        ans = []
        def possibles(tstr,i):
            if i>=l:
                ans.append(tstr)
                return None

            for c in dic[digits[i]]:
                possibles(tstr+c,i+1)

        possibles("",0)

        return ans




# 执行用时为 20 ms 的范例
# class Solution:
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         result = []
#         if len(digits) == 0:
#             return result
        
#         int_to_char = {'2': ['a', 'b', 'c'],
#                        '3': ['d', 'e', 'f'],
#                        '4': ['g', 'h', 'i'],
#                        '5': ['j', 'k', 'l'],
#                        '6': ['m', 'n', 'o'],
#                        '7': ['p', 'q', 'r', 's'],
#                        '8': ['t', 'u', 'v'],
#                        '9': ['w', 'x', 'y', 'z']}
        
#         # backtracking function
#         def f(s, idx):
#             if idx == len(digits):
#                 result.append(s)
#             else:
#                 for char in int_to_char[digits[idx]]:
#                     f(s+char, idx+1)
#         f('', 0)
#         return result