# leetcode-434-字符串中的单词数.py
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

# 请注意，你可以假定字符串里不包括任何不可打印的字符。

# 示例:

# 输入: "Hello, my name is John"
# 输出: 5


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())



