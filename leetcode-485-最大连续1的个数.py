# leetcode-485-最大连续1的个数.py
# 给定一个二进制数组， 计算其中最大连续1的个数。

# 示例 1:

# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：

# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。

"""
思路:
这..

跳记

index

范例的 "快速" 看不太懂呢..

len vs for ??
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        i = 0
        maxcount = 0
        count = 0
        while i<l:
            while i<l and nums[i]==0:
                i+=1
            s = i

            while i<l and nums[i]==1:
                i+=1
            count = i-s

            maxcount = max(maxcount,count)

        return maxcount


执行用时为 72 ms 的范例
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t,mx=0,0
        for i in nums:
            if i == 1:
                t = t+1
            else:
                mx = t if t > mx else mx
                t=0
        return max(mx,t)