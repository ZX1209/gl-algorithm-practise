# leetcode-169-求众数.py
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在众数。

# 示例 1:

# 输入: [3,2,3]
# 输出: 3
# 示例 2:

# 输入: [2,2,1,1,1,2,2]
# 输出: 2

"""
思路:
可以,,直接count吧..

出现次数大于 n/2 的下界..嗯..可以优化下...

啊啊啊啊啊,,直接排序更方便啊啊啊啊啊啊啊啊啊啊

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}
        l = len(nums)
        half = int(l/2)

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

            if dic[num] > half:
                return num


# 参考 
# 执行用时为 32 ms 的范例
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return nums[len(nums)/2]

