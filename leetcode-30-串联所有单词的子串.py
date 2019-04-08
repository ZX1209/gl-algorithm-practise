# leetcode-30-串联所有单词的子串.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

# 示例 1：

# 输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2：

# 输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]

"""
思路:
单词重叠??

长度相同的words?
恰好可以由words中所有单词串联形成的子串?
长度就固定了.

找子串

子串符合一定规律

组合 再 查找?
"""

class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        if not words or len(s)<len(words)*len(words[0]):
            return []

        wl = len(words[0])
        i = 0
        tmpset = Counter(words)
        results = []
        start = i

        # 遍历 s
        while i<len(s):
            # 如果 这个单词 是需要的
            if s[i:i+wl] in tmpset:
                tmpset[s[i:i+wl]] -= 1
                if tmpset[s[i:i+wl]]<=0:
                    del tmpset[s[i:i+wl]]

                # 是否全部符合
                if tmpset == Counter():
                    results.append(start)
                    tmpset = Counter(words)
                    i = start
                    start = i+wl
                i+=wl
            # 否则,找到需要的
            else:
                tmpset = Counter(words)
                i = start+1
                while i<len(s):
                    if i+wl<len(s) and s[i:i+wl] in words:
                        start = i
                        break
                    i+=1
        return results


# 参考
# 滑动窗口?
class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        if not words or len(s)<len(words)*len(words[0]):
            return []
        result = []
        word_len = len(words[0])

        for stripe in range(word_len): # each stripe starts at a different position in s, modulo word_len
            i = stripe # the next index in s that we want to match a word
            to_match = len(words) # number of words still to be matched
            freq = Counter(words) # frequency of each words to be matched

            while i+to_match*word_len<=len(s): #remainder fo s is long enough to hold remaining unmatched words
                word = s[i:i+word_len] # next part of s attempting to be matched
                if word in freq: # match, decrement freq count
                    freq[word]-=1
                    if freq[word]<=0:
                        del freq[word]

                    to_match -= 1
                    i+=word_len
                    if to_match == 0: # all matched
                        result.append(i-word_len*len(words))
                elif to_match != len(words): # some words have been matched
                    nb_matches = len(words) - to_match
                    first_word = s[i-nb_matches*word_len:i-(nb_matches-1)*word_len]
                    freq.setdefault(first_word,0)
                    to_match+=1
                else:
                    i+=word_len
        return result

# 执行用时为 64 ms 的范例
class Solution:
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        lens = len(s)
        lenw = len(words[0])
        lenws = lenw * len(words)
        if lens < lenws:
            return []
        counter = {}
        for i in range(len(words)):
            if words[i] in counter:
                counter[words[i]] += 1
            else:
                counter[words[i]] = 1
        res = []
        for i in range(min(lenw, lens-lenws + 1)):
            s_pos = word_pos = i
            d = {}
            while s_pos + lenws <= lens:
                # 截取单词
                word = s[word_pos:word_pos + lenw]
                # 移动到下一个单词
                word_pos += lenw
                if word not in counter:
                    s_pos = word_pos
                    d.clear()
                else:
                    if word not in d:
                        d[word] = 1
                    else:
                        d[word] += 1
                    while d[word] > counter[word]:
                        d[s[s_pos:s_pos + lenw]] -= 1
                        s_pos += lenw
                    if word_pos - s_pos == lenws:
                        res.append(s_pos)
        return res

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    test = Solution()
    r = test.findSubstring(s,words)
    print(r)

