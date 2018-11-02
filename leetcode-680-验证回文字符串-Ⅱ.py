# leetcode-680-验证回文字符串-Ⅱ.py
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

# 示例 1:

# 输入: "aba"
# 输出: True
# 示例 2:

# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 注意:

# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

"""
思路:
最后删除一个字符,判断是否能成为回文串

先判断,,是不是
在试试要删一个的..

删除后的时候是回文串..

从左右,到中,
要是里面的删除的是回文,整个也就是回文..
"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 参考    
        n = len(s)
        i = 0

        while i<n//2:
            if s[i] != s[n-1-i]:
                del_front = s[i+1:n-i]
                del_back = s[i:n-i-1]
                return del_front == del_front[::-1] or del_back == del_back[::-1]
            i+=1
        return True

        # if s == s[::-1]:
        #     return True

        # s = list(s)
        # l = len(s)
        # if l<=2:
        #     return True

        # i = (l//2)-1
        # j = l//2

        # if l%2:
        #     j+=1

        # modified = False 
        # if l%2==0 and s[i]!=s[j]:
        #     modified = True
        #     i-=1
        #     j+=1
        # while i>=0 and j<l:
        #     if s[i]!=s[j]:
        #         if modified:
        #             return False
        #         if j+1<l and s[i]==s[j+1]:
        #             j+=1
        #             modified = True
        #         elif 0<=i-1 and s[j]==s[i-1]:
        #             i-=1
        #             modified = True
        #         elif i-1<0 and j+1>=l:
        #             return True
        #         else:
        #             return False

        #     i-=1
        #     j+=1

        # return True




执行用时为 84 ms 的范例
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = s[::-1]
        if a == s:
            return True
        for i in range(len(s)):
            if s[i] != a[i]:
                temp_1 = s[:i] + s[i+1:]
                temp_2 = a[:i] + a[i+1:]
                return temp_1 == temp_1[::-1] or temp_2 == temp_2[::-1]