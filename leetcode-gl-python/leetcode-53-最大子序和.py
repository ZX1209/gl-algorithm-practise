# leetcode-53-最大子序和.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""
思路,总结:
这个,,原先思路有些失败呢..嗯,,条件判断也要很讲究呢....

"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        maxsum = nums[0]
        tmpsum = 0

        for i in range(l):
            tmpsum += nums[i]

            if tmpsum > maxsum:
                maxsum = tmpsum

            if tmpsum<0:
                tmpsum = 0

        return maxsum


if __name__ == '__main__':
    test = Solution()
    test.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])


# 参考
# 执行用时为 40 ms 的范例
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sum = 0
#         max = nums[0]
        
#         for index in range(len(nums)):
#             if sum < 0:
#                 sum = 0

#             sum += nums[index]
            
#             if sum > max:
#                 max = sum
        
#         return max