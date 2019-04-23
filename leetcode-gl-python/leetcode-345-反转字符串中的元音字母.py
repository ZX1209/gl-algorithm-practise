# leetcode-345-反转字符串中的元音字母.py
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

# 示例 1:

# 输入: "hello"
# 输出: "holle"
# 示例 2:

# 输入: "leetcode"
# 输出: "leotcede"
# 说明:
# 元音字母不包含字母"y"。


"""
思路:
a e i o u

从后往前,从前往后

大小写??
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = len(s)

        yun = set(('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'))

        i = 0
        j = l-1

        while i < j:
            while i < j:
                if s[i] in yun:
                    break
                i += 1

            while i < j:
                if s[j] in yun:
                    break
                j -= 1

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)