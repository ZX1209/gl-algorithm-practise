# leetcode-219-存在重复元素-II.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

# 示例 1:

# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 示例 2:

# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 示例 3:

# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false


"""
思路:
defaultdic??

其实也不用特别用list啦
"""

from collections import defaultdict

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = defaultdict(list)

        for i,v in enumerate(nums):
            if v in dic:
                if abs(dic[v][-1] - i)<= k:
                    return True
                else:
                    dic[v].append(i)
            else:
                dic[v].append(i)

        return False



# 参考
# 执行用时为 28 ms 的范例
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         d = {}
#         t = 0
#         for i in xrange(len(nums)):
#             t = nums[i]
#             if not t in d or i-d[t] > k:
#                 d[t] = i
#             else:
#                 return True
#         return False