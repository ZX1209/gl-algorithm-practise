# leetcode-字谜分组.py
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：

# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

"""
思路:
长度,~集合~,,count

en ..
想到了排序整个strs
但没有想到排序单个str呢...

看清关键再哪喽..

解答即参考...

"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # 参考
        sorted_words = defaultdict(list)

        for word in strs:
            sorted_list = [c for c in word]
            sorted_list.sort()
            sorted_word = "".join(sorted_list)

            sorted_words[sorted_word].append(word)

        return list(sorted_words.values())



        # i = 0
        # ans = []

        # while i<len(strs):
        #     tmps = strs[i]
        #     ans.append([strs[i]])
        #     strs.pop(i)

        #     j = i
        #     while j<len(strs):
        #         if len(tmps) == len(strs[j]):
        #             if not any([tmps.count(c) != strs[j].count(c) for c in set(tmps)]):
        #                 ans[-1].append(strs[j])
        #                 strs.pop(j)
        #                 j-=1

        #         j += 1

        # return ans