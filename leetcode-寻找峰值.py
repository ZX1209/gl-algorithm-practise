# # leetcode-寻找峰值.py
# 峰值元素是指其值大于左右相邻值的元素。

# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞。

# 示例 1:

# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:

# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5 
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:

# 你的解法应该是 O(logN) 时间复杂度的。


"""
思路:
最小值??

左右负无穷呢.

下滑??上升??

下滑不行,,负无穷会破坏完整性

上升可以在..最大值也可以呢..

嗯,,说返回任意个,就可以知道有什么其他方法了..

这是二分??为什么??
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        i = 0

        while i<l-1:
            if nums[i]>nums[i+1]:
                break
            i += 1

        return i

if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    test = Solution()
    r = test.findPeakElement(nums)
    print(r)



# 执行用时为 20 ms 的范例
# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         >>> Solution().findPeakElement([1,2,3,1])
#         2
#         >>> Solution().findPeakElement([1,2])
#         1
#         """
#         left, right = 0, len(nums)-1
#         while left < right:
#             mid = (left + right) // 2
#             if mid == len(nums)-1:
#                 return mid

#             if nums[mid] < nums[mid+1]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return right