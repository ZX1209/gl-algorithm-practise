# leetcode-349-两个数组的交集.py
# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1:

# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
# 示例 2:

# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
# 说明:

# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。


"""
思路:
排序??

yes


还是没看清题目呢..
"""



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        l1 = len(nums1)
        l2 = len(nums2)

        ans = set()

        i = 0
        j = 0
        while i<l1 and j<l2:
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif  nums1[i] < nums2[j]:
                i += 1

        return list(ans)


# 参考
# 行用时为 24 ms 的范例
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         nums1 = set(nums1)
#         return [x for x in set(nums2) if x in nums1]

