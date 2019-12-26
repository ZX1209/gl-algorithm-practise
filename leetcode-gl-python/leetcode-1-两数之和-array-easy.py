#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (47.16%)
# Likes:    7228
# Dislikes: 0
# Total Accepted:    740.3K
# Total Submissions: 1.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#
from typing import List


# @lc code=start
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = sorted(nums)

        for i in range(len(snums)):
            for j in range(len(snums) - 1, i, -1):
                if snums[i] + snums[j] > target:
                    continue
                elif snums[i] + snums[j] == target:
                    ai = nums.index(snums[i])
                    aj = nums.index(snums[j])
                    if aj == ai:
                        aj = nums.index(snums[j], ai + 1)

                    return [ai, aj]
                elif snums[i] + snums[j] < target:
                    break

        return [0, 0]


# the use of map and in
# class Solution:
#     # @return a tuple, (index1, index2)
#     # 8:42
#     def twoSum(self, num, target):
#         map = {}
#         for i in range(len(num)):
#             if num[i] not in map:
#                 map[target - num[i]] = i
#             else:
#                 return map[num[i]], i

#         return -1, -1

# @lc code=end

if __name__ == "__main__":
    nums = [-1, -2, -3, -4, -5]
    tar = -8
    test = Solution()
    print(test.twoSum(nums, tar))
