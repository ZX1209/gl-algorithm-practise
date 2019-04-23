# leetcode-前K个高频元素.py
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

# 示例 1:

# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:

# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：

# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。


"""
思路:
这,Counter??

字典值吗,,还有sort..也行..计数了就好..
"""

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        ans = []
        for one in c.most_common(k):
            ans.append(one[0])

        return ans




# 执行用时为 32 ms 的范例
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         freq = dict()  
#         for n in nums:
#             if n in freq:
#                 freq[n] += 1
#             else:
#                 freq[n] = 1
#         res = sorted(freq, key=lambda x: (-freq[x], x))
#         return res[0:k]