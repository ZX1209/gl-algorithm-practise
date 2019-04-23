# leetcode-数组中的第K个最大元素.py
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:

# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。



"""
思路:
竟然感觉冒泡排序不错呢..

heapq?

范例2不怎看的懂呢..
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ans = heapq.nlargest(k,nums)
        return ans[-1]


# 执行用时为 28 ms 的范例
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         return sorted(nums)[-k]


# 执行用时为 36 ms 的范例
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         # return sorted(nums)[-k]
#         def perc_down(arr,start,end):
#             root=start
#             while True:
#                 child=2*root+1
#                 if child>end:
#                     break
#                 elif child+1<=end and arr[child]>arr[child+1]:
#                     child+=1
#                 if arr[child]<arr[root]:
#                     arr[root],arr[child]=arr[child],arr[root]
#                     root=child
#                 else:
#                     break
#         n=len(nums)
#         for i in range((k-2)//2,-1,-1):
#             perc_down(nums,i,k-1)
#         for j in range(k,n):
#             if nums[j]>nums[0]:
#                 nums[0]=nums[j]
#                 perc_down(nums,0,k-1)
#         return nums[0]

