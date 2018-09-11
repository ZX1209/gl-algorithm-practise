# leetcode-只出现一次的数字.py
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:

# 输入: [2,2,1]
# 输出: 1
# 示例 2:

# 输入: [4,1,2,1,2]
# 输出: 4

"""
思路:
出现奇数次,偶数次???

可以,,count..但会超时吧.

遍历?不行


"""
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # slow
        # for n in set(nums):
        #     if nums.count(n) == 1:
        #         return n

        c = Counter(nums)

        return c.most_common()[-1][0]


# 参考
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sum = 0
#         for i in nums:
#             sum = sum ^ i
#         return sum  