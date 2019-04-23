# leetcode-521-最长特殊序列-1.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

# 子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

# 输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。

# 示例 :

# 输入: "aba", "cdc"
# 输出: 3
# 解析: 最长特殊序列可为 "aba" (或 "cdc")
# 说明:

# 两个字符串长度均小于100。
# 字符串中的字符仅含有 'a'~'z'

"""
思路:
这是语言题吧..
"""

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a==b:
            return -1
        else:
            return max(len(a),len(b))


执行用时为 36 ms 的范例
class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))