# leetcode-628-三个数的最大乘积.py
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

# 示例 1:

# 输入: [1,2,3]
# 输出: 6
# 示例 2:

# 输入: [1,2,3,4]
# 输出: 24
# 注意:

# 给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


"""
思路:
三个数组成的最大乘积,还是在有负数的情况下呢..
正数一组
负数一组??
"""

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        # 全正
        if nums[0]>=0:
            return nums[-1]*nums[-2]*nums[-3]
        # 全 负
        elif nums[-1]<=0:
            return nums[-1]*nums[-2]*nums[-3]
        else:
            if nums[0]*nums[1]>nums[-2]*nums[-3]:
                return nums[0]*nums[1]*nums[-1]
            else:
                return nums[-1]*nums[-2]*nums[-3]



执行用时为 72 ms 的范例
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = -sys.maxsize
        max_2 = -sys.maxsize
        max_3 = -sys.maxsize
        min_1 = sys.maxsize
        min_2 = sys.maxsize
        for num in nums:
            if num > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_3 = max_2
                max_2 = num
            elif num > max_3:
                max_3 = num
            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num
        return max(max_1 * max_2 * max_3, max_1 * min_1 * min_2)

执行用时为 80 ms 的范例
import heapq
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a1,a2,a3 = heapq.nlargest(3,nums)
        l1,l2 = heapq.nsmallest(2,nums)
        return max(a1*a2*a3,a1*l1*l2)