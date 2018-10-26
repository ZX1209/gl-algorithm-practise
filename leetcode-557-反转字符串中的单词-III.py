# leetcode-557-反转字符串中的单词-III.py
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例 1:

# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

"""
思路:
要保持空格的话..
stack??

generator 比 直接加要快吗
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # formal
        # s = list(s)

        # i = 0
        # l = len(s)
        # S = []
        # ans = []
        # while i<l:
        #     if s[i]==' ':
        #         ans.extend(S[::-1])
        #         S.clear()
        #         ans.append(s[i])
        #     elif i==l-1:
        #         S.append(s[i])
        #         ans.extend(S[::-1])
        #         S.clear()
        #     else:
        #         S.append(s[i])

        #     i+=1

        # return "".join(ans)







        # slist = s.split(' ')
        # i= 0
        # l = len(slist)
        # while i<l:
        #     slist[i] = slist[i][::-1]
        #     i+=1

        # return " ".join(slist)

执行用时为 36 ms 的范例
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        for a in range(len(l)):
            l[a]=l[a][::-1]
        return ' '.join(l)    