# leetcode-存在重复.py
# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: true
# 示例 2:

# 输入: [1,2,3,4]
# 输出: false
# 示例 3:

# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true

"""
思路:
首先,前面出现的数字肯定要记录..

可以直接转化为集合,
长度相减

优化??

毕竟只是简单题..
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(nums) - len(set(nums)) != 0

# 参考
# 执行用时为 32 ms 的范例
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         a=set(nums)
#         if nums==[]:
#             return False
#         else:
#             if len(a)!=len(nums):
#                 return True
#             else:
#                 return False