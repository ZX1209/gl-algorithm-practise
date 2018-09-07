# leetcode-58-最后一个单词的长度.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

# 如果不存在最后一个单词，请返回 0 。

# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。

# 示例:

# 输入: "Hello World"
# 输出: 5

"""
思路:
en ~~
最好先去两边的空格,,
去掉特殊情况
之后,从后往前数...


"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == "":
            return 0

        s = s.split()
        if len(s)>0:
            return len(s[-1])
        else:
            return 0


# 执行用时为 36 ms 的范例
# class Solution:
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s is None:
#             return 0
#         s_arr = s.split()
#         return len(s_arr[-1]) if len(s_arr) > 0 else 0