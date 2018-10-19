# leetcode-496-下一个更大元素-I.py
# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

# 示例 1:

# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
#     对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
#     对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
# 示例 2:

# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于num1中的数字2，第二个数组中的下一个较大数字是3。
#     对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
# 注意:

# nums1和nums2中所有元素是唯一的。
# nums1和nums2 的数组大小都不超过1000。

"""
思路:
write it

note 解法.
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []
        for num in nums1:
            targetIndex = nums2.index(num)
            try:
                i = targetIndex+1
                while nums2[i]<=num:
                    i+=1
                ans.append(nums2[i])
            except :
                ans.append(-1)

        return ans


执行用时为 44 ms 的范例
class Solution:
    def nextGreaterElement(self, findNums, nums):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]


执行用时为 48 ms 的范例
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        d = {}
        s = []
        for i in nums2:
            while s and s[-1] < i:
                d[s.pop()] = i
            s.append(i)
            
        return [d.get(i, -1) for i in nums1]