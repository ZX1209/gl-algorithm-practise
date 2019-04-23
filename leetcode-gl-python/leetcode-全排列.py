# leetcode-全排列.py
# 给定一个没有重复数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

"""
思路:
虽然,,可以用,,什么,,product,,

自己试试??

全局轴,局部轴??
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = set(nums)
        ans = []

        def combination(the_nums,combinalist):
            if len(the_nums)<=0:
                ans.append(combinalist)
            for num in the_nums:
                combination(the_nums-{num},combinalist+[num])
        combination(nums,[])

        return ans



# 执行用时为 40 ms 的范例
# s = []

# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         def dfs():
#             global s
#             if nums == []:
#                 ans.append(s)
#             else:
#                 for e in nums:
#                     s.append(e)

#                     nums.remove(e)
#                     dfs()

#                     s = s[0:len(s)-1]
#                     nums.append(e)
#                     nums.sort()
#         if nums == []:
#             return []
#         ans = []
#         nums.sort()
        
#         dfs()
        
#         return ans


