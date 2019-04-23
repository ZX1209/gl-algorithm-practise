# leetcode-709-转换成小写字母.py
# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

 

# 示例 1：

# 输入: "Hello"
# 输出: "hello"
# 示例 2：

# 输入: "here"
# 输出: "here"
# 示例 3：

# 输入: "LOVELY"
# 输出: "lovely"


class Solution:
    def toLowerCase(self, tstr):
        """
        :type str: str
        :rtype: str
        """
        return tstr.lower()


执行用时为 32 ms 的范例
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()