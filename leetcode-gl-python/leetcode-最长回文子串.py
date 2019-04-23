# leetcode-最长回文子串.py
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"


"""
思路:
也是双指针,,但是后面就是闭合遍历了..吧..
不行,,这种方法只适合,回文串在后面的,,

通过解答即参考

leetcode参考,,,嗯,,.................


"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""


        centers = [len(s)-1]
        for diff in range(len(s)):
            centers.append(centers[0]+diff)
            centers.append(centers[0]-diff)

        for center in centers:
            if min(center+1,2*len(s)-1-center) <= len(longest):
                break
            if center % 2 == 0:
                left,right = (center // 2)-1,(center // 2)+1
            else: 
                left,right = (center // 2),(center // 2)+1

            while left >= 0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left -1 > len(longest):
                longest = s[left+1:right]

        return longest

        # l = len(s)

        # if l<=1:
        #     return s

        # start = 0
        # end = l-1
        # longest = ""

        # while start<end:
        #     while end>start and s[end] != s[start]:
        #         end -= 1

        #     # below s[end] == s[start] or end <= start
        #     i = start
        #     j = end
        #     while j>i and s[j] == s[i]:
        #         j = j - 1
        #         i = i + 1

        #     if j<=i:
        #         if len(longest)<len(s[start:end+1]):
        #             longest = s[start:end+1]
        #     end = l-1
        #     start+=1

        # return longest

if __name__ == '__main__':
    s = "aaabaaaa"
    test = Solution()
    r = test.longestPalindrome(s)
    print(r)


# leetcode 参考 
# 执行用时为 48 ms 的范例
# #coding=utf-8
# class Solution(object):
#     def longestPalindrome(self,s):
#         if s == s[::-1]:
#             return s
#         maxlen = 1
#         start = 0
#         for i in xrange(len(s)):
#             if i - maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
#                 start = i - maxlen - 1
#                 maxlen += 2
#                 continue
#             if i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
#                 start = i - maxlen
#                 maxlen += 1
               
            
#         return s[start:start+maxlen]