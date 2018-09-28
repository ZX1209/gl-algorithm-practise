# leetcode-搜索旋转排序数组.py
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:

# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:

# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


"""
思路:
就是给出一个特别的规律的数组吧..

然后,找目标值..

限制使用二分法??

但是旋转的意思是??

也不是不可以二分呢...

又是tmd特殊情况,,,没有意思...

二分,分情况...
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if nums==[]:
        #     return -1
        # right = nums[-1]

        # if right>target:
        #     i = len(nums)-2
        #     while i>0:
        #         if nums[i]>right:
        #             return -1
        #         elif nums[i] == target:
        #             return i
        #         i -=1
        # elif right < target:
        #     i = 0
        #     while i<len(nums):
        #         if nums[i]<right:
        #             return -1
        #         elif nums[i] == target:
        #             return i
        #         i += 1
        # else:
        #     return len(nums)-1

        try:
            return nums.index(target)
        except:
            return -1



执行用时为 20 ms 的范例
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1