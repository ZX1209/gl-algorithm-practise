# leetcode-389-找不同.py
# 给定两个字符串 s 和 t，它们只包含小写字母。

# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

# 请找出在 t 中被添加的字母。

 

# 示例:

# 输入：
# s = "abcd"
# t = "abcde"

# 输出：
# e

# 解释：
# 'e' 是那个被添加的字母。

"""
思路:
排序,搜索?

字典?

集?

count?

嗯,,pythonic..效率不太好估算啊..内置函数效率高太多了..


"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss = set(s)
        st = set(t)

        if st-ss == set():
            dic = {}
            for c in st:
                dic[c] = t.count(c)
                if s.count(c) != dic[c]:
                    return c

        else:
            return (st-ss).pop()


# 参考 
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         n = ''
#         for i in set(t):
#             n += ''.join(i)
#         for j in n:
#             if s.count(j) != t.count(j):
#                 return j

