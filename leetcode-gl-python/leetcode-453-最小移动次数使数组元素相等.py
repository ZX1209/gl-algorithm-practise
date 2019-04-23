# leetcode-453-最小移动次数使数组元素相等.py
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。

# 示例:

# 输入:
# [1,2,3]

# 输出:
# 3

# 解释:
# 只需要3次移动（注意每次移动会增加两个元素的值）：

# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


"""
思路:
每次n-1个值,,这是个数学题把...

从小到大,,添加??直到相等??

反向减??
可以,反向减,,我的其实也可以优化,,不用一个个减了,,傻了..
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        m = min(nums)
        count = 0
        for num in nums:
            count+=num-m
        return count


执行用时为 36 ms 的范例
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)