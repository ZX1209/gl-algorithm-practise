# leetcode-438-找到字符串中所有字母异位词.py
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

# 说明：

# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 示例 1:

# 输入:
# s: "cbaebabacd" p: "abc"

# 输出:
# [0, 6]

# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  示例 2:

# 输入:
# s: "abab" p: "ab"

# 输出:
# [0, 1, 2]

# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。


"""
思路:
字母异位词.. 
排排序可以判定..

参考维护了一个,字符频率表.

啊,关键数据.. 
"""


# 参考
from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        freq = defaultdict(int)
        result = []

        if n>len(s):
            return result

        def update_freq(c,step):
            freq[c]+=step 
            if freq[c] == 0:
                del freq[c]

        for c1,c2 in zip(p,s[:n]):
            update_freq(c1,-1)
            update_freq(c2,1)

        for i in range(len(s)-n):
            if not freq:
                result.append(i)
            update_freq(s[i],-1)
            update_freq(s[i+n],1)

        if not freq:
            result.append(len(s)-n)

        return result

        # # most easy search all
        # if len(s)<=0 or len(p)<=0:
        #     return []
        # sp = sorted(p)
        # lp = len(p)
        # ans = []
        # for i  in range(0,len(s)-lp+1):
        #     if sorted(s[i:i+lp]) == sp:
        #         ans.append(i)

        # return ans

        # my failure
        # ls = len(s)
        # lp = len(p)
        # tp = list(p)

        # start = 0
        # end = 0
        # ans = []

        # while start<=end<ls:
        #     while start<ls and s[start] not in p:
        #         start+=1
        #     end = start

        #     while end<ls and s[end] in tp:
        #         tp.remove(s[end])
        #         end+=1
        #     # below s[end] not i tp or tp==[] or end>ls
        #     if tp==[]:
        #         ans.append(start)
        #     else:
        #         start+=1

        #     tp = list(p)

        # return ans


# 执行用时为 96 ms 的范例
# class Solution(object):
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
        
#         sizep = len(p)
#         sizes = len(s)
        
#         p = "".join(sorted(p))
#         ans = []
        
#         if sizes < sizep:
#             return []
#         if sizep == sizes:
#             return [0] if "".join(sorted(s)) == p else []
        
#         check = lambda x,y:  "".join(sorted(x)) == y
        
#         i = 0
#         while 1:
#             while check(s[i:i+sizep], p) is False:
#                 i += 1
#                 while i + sizep <= sizes and s[i] not in p:
#                     i += 1
#                 if i+sizep > sizes:
#                     return ans
                
#             ans.append(i)

#             if i+sizep < sizes: 
           
#                 while s[i+sizep] == s[i]:
#                     i += 1
#                     ans.append(i)
                    
#                     if i+sizep >= sizes:
#                         return ans
#                 tmp = i+sizep
#                 while s[i] != s[tmp]:
#                     i += 1
                        
#             else:
#                 return ans
        
            