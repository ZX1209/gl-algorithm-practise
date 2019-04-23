# leetcode-290-单词模式.py
# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

# 示例1:

# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:

# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:

# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 示例 4:

# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。  



"""
思路:
双向连接!!!!!

代码缩进..这..

参考不错啊..len..长度,,转换的关键
"""

class Solution(object):
    def wordPattern(self, pattern, strs):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = strs.split()
        l = len(pattern)
        l2 = len(strs)
        if l != l2:
            return False

        dic = {}

        i = 0
        while i<l:
            # 键中存在
            ## 值相同
            ## 值不相同
            # 值存在
            ## 键相同
            ## 键不相同
            if pattern[i] in dic:
                if dic[pattern[i]] != strs[i]:
                    return False
            else:
                if strs[i]  in dic.values():
                    return False
                else:
                    dic[pattern[i]] = strs[i]

            i += 1

        return True



# 参考
# 执行用时为 20 ms 的范例
# class Solution(object):
#     def wordPattern(self, pattern, str):
#         """
#         :type pattern: str
#         :type str: str
#         :rtype: bool
#         """
#         strlist = str.split()
        
#         if len(pattern) != len(strlist):
#             return False
#         return (len(set(pattern))) == (len(set(strlist))) == (len(set(zip(pattern, strlist))))


