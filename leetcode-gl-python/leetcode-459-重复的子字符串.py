# leetcode-459-重复的子字符串.py
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

# 示例 1:

# 输入: "abab"

# 输出: True

# 解释: 可由子字符串 "ab" 重复两次构成。
# 示例 2:

# 输入: "aba"

# 输出: False
# 示例 3:

# 输入: "abcabcabcabc"

# 输出: True

# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)


"""
思路:
这,要先看长度,分组..  嗯..??
滑窗??

中分,??

既然是由子串重复多次构成的,,那么,

跳连?试着构造全部.. 1...1...1...1..2..x

范例是??真的可以.. 
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l<=1:
            return False


        for div in range(1,(l//2)+1):
            # 是否能整除,,是否能分组
            if l%div:
                continue
            else:
                # 分组都一样
                if all([s[i:i+div] == s[0:div] for i in range(div,l,div)]):
                    return True

        return False


执行用时为 28 ms 的范例
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s * 2)[1:-1]
        #print ss
        return s in ss

if __name__ == '__main__':
    s = "babbabbabbabbab"
    test = Solution()
    r = test.repeatedSubstringPattern(s)
    print(r)
