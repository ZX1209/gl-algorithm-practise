# leetcode-旋转数组.py
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:

# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:

# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。


"""
先暴力的试试..

还有一个类似旋转角的优化..


直接移k个数..

拼接,,不错..
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        # -1, -2, -3, -4, ...
        # 0, 1, 2, 3, 4, 5

        tmpList = nums[-k::1]

        nums[k:] = nums[:-k]

        nums[:k] = tmpList


# 参考
# 执行用时为 48 ms 的范例
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
       
#         nums_len = len(nums)
#         nums[:] = nums[nums_len - k :] + nums[:nums_len - k]


