# leetcode-无重复字符的最长子串.py
# 给定一个字符串，找出不含有重复字符的最长子串的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 无重复字符的最长子串是 "abc"，其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 无重复字符的最长子串是 "b"，其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 无重复字符的最长子串是 "wke"，其长度为 3。
#      请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

"""
思路:
这个,,双指针遍历..


循环增量!!!!!!!!!!!!!!

还是要先解决特殊量呢..真事的

嗯,,应该从第一个重复位前开始的啊..

en ,,想到怎么做,,但是没有适当的表达出来的呢..

通过代码即参考
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        start = 0
        longest = 0

        for i,c in enumerate(s):

            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c]+1
            else:
                longest = max(longest,i-start+1)
            last_seen[c] = i

        return longest

        # l = len(s)
        # if l == 0:
        #     return 0
        # elif l == 1:
        #     return 1


        # ans = 0
        # i = 0
        # j = 0

        # while i<l:
        #     while j<l and s[j] not in s[i:j]:
        #         j+=1

        #     # below s[j] in s[i:j] [i,j)
        #     # or j == l

        #     if j>=l:
        #         j = l-1


        #     if ans < j-i:
        #         ans = j - i



        #     while i<j and s[i] != s[j]:
        #         i+=1
        #     # below s[i] == s[j]
        #     i+=1

        # return ans+1