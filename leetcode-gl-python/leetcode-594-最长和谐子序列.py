# leetcode-594-最长和谐子序列.py
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

# 示例 1:

# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
# 说明: 输入的数组长度最大不超过20,000.


"""
思路:
子序列可以不是连续的

最大值和最小值之间差1嗯,,找到两个相邻的数,且数量最多

in..
"""

from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = Counter(nums)
        maxans = 0
        for k in c.keys():
            if c[k+1] !=0:
                if maxans<c[k]+c[k+1]:
                    maxans=c[k]+c[k+1]

            if c[k-1] !=0:
                if maxans<c[k]+c[k-1]:
                    maxans=c[k]+c[k-1]
        return maxans


执行用时为 96 ms 的范例
from collections import Counter
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_n = Counter(nums)
        max_l = 0
        for k, v in c_n.items():
            if (k+1) in c_n and v+c_n[k+1] > max_l:
                max_l = v+c_n[k+1]
        return max_l
        