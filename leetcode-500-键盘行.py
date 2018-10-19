# leetcode-500-键盘行.py
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。


# American keyboard


# 示例：

# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]


# 注意：

# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。

"""
思路:
set??

状态赋值
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        keysets = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                   {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                   {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]

        for word in words:
            tmpset = set(word.lower())
            for keyset in keysets:
                if keyset>=tmpset:
                    ans.append(word)

        return ans



执行用时为 36 ms 的范例
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret=[]
        for word in words:
            count = 0
            for letter in word:
                if letter in 'qwertyuiop' or letter in 'QWERTYUIOP':
                    if count==0 or count==1:
                        count=1
                    else:
                        break
                elif letter in'asdfghjkl' or letter in 'ASDFGHJKL':
                    if count==0 or count==2:
                        count=2
                    else:
                        break
                else:
                    if count==0 or count==3:
                        count=3
                    else:
                        break
            else:
                ret.append(word)
        return ret