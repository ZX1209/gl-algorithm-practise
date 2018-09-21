# leetcode-383-赎金信.py
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

# 注意：

# 你可以假设两个字符串均只含有小写字母。

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


"""
思路:
寻找??

不清晰啊..
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        l = len(ransomNote)
        l2 = len(magazine)

        i = 0
        j = 0 
        while i<l and j<l2:
            if magazine[j]<ransomNote[i]:
                j += 1
            elif magazine[j]==ransomNote[i]:
                i += 1
                j += 1
            else:
                break


        return i == l


# 参考 
# 执行用时为 36 ms 的范例
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         x=set(i for i in ransomNote)
#         dic={}
#         for i in x:
#             dic[i]=ransomNote.count(i)
#         for k,v in dic.items():
#             if magazine.count(k)<v:
#                 return False
#         return True