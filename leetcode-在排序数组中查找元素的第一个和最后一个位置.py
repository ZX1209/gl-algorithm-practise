# leetcode-在排序数组中查找元素的第一个和最后一个位置.py
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 如果数组中不存在目标值，返回 [-1, -1]。

# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:

# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


"""
思路:
二分,双指针??
中分?

二分查找,,在从中到左右..嗯,思路一样呢..
但是为什么效率差那么多呢.??
函数?try?


"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        try:
            i = nums.index(target)
            end = i 
            start = i
        except ValueError:
            return [-1,-1]

        while end<len(nums) and nums[end]==target:
            end += 1

        return [start,end-1]



# 执行用时为 24 ms 的范例
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if not nums:
#             return [-1, -1]
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) / 2
#             if nums[mid] == target:
#                 left = mid
#                 right = mid
#                 while left >= 0 and nums[left] == target:
#                     left -= 1
#                 while right <= len(nums) - 1 and nums[right] == target:
#                     right += 1
#                 return [left + 1, right - 1]
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return [-1,-1]

