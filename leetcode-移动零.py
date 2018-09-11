# leetcode-移动零.py
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

"""
思路:
嗯,,原数组上操作..
减少移动次数

一般是不会用删除什么的吧..
虽说挺方便的

先用下吧..

果然高效的是直接移动啊
或者说交换下..可以
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0
        while True:
            try:
                nums.remove(0)
                count+=1
            except ValueError:
                nums.extend([0]*count)
                break

# 参考
# 执行用时为 40 ms 的范例
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """ 
#         i = j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1