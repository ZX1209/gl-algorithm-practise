# leetcode-缺失数字.py
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

# 示例 1:

# 输入: [3,0,1]
# 输出: 2
# 示例 2:

# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

"""
思路:
断层..

嗯,,没有想到和或者乘啊..
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 0:
            return 0
        elif len(nums) ==1:
            return 1-nums[0]
        else:
            nums.sort()

            if nums[0]!=0 :
                return 0

            for i in range(1,len(nums)):
                if nums[i-1]+1 != nums[i]:
                    return nums[i-1]+1

            if nums[-1] != len(nums):
                return nums[-1]+1

            return -1


# 参考
# 执行用时为 32 ms 的范例
# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums is None or len(nums) == 0:
#             return 0
#         length = len(nums)
#         sum = int(length * (length + 1) / 2)
#         sub_sum = 0
#         for i in nums:
#             sub_sum += i

#         return sum - sub_sum