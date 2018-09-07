leetcode-14-最长公共前缀.py


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""

        minl = len(strs[0])
        for str in strs:
            if minl > len(str):
                minl = len(str)

        ans_str = ""

        for i in range(minl):
            for str in strs[1:]:
                if str[i] != strs[0][i]:
                    return ans_str

            ans_str = ans_str + strs[0][i]

        return ans_str


# 执行用时为 36 ms 的范例
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
#         shortest=min(strs,key=len)
#         for x, y in enumerate(shortest):
#             for s in strs:
#                 if s[x]!=y:
#                     return shortest[:x]
#         return shortest
