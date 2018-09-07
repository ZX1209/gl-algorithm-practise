# leetcode-35-搜索插入位置.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 示例 1:

# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:

# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:

# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:

# 输入: [1,3,5,6], 0
# 输出: 0


"""
思路:
这,,直接查,插??
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = len(nums)
        insert_index = -1

        for i in range(l):
            if nums[i] == target:
                return i

            elif nums[i] < target:
                insert_index = i

        return insert_index + 1


# 参考

# 执行用时为 36 ms 的范例


# class Solution:
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """

#         if target in nums:
#             return nums.index(target)
#         i, j = 0, len(nums) - 1
#         while i < j:
#             mid = (j - i) // 2 + i
#             if nums[mid] < target:
#                 i = mid + 1
#             else:
#                 j = mid - 1
#         return i if nums[i] > target else i + 1
