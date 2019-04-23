# leetcode-665-非递减数列.py
# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

# 示例 1:

# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 示例 2:

# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 说明:  n 的范围为 [1, 10,000]。

"""
思路:
还是模拟吗??
"""


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified = False

        for i,num in enumerate(nums[1:],1):
            if nums[i-1]>num:
                if modified:
                    return False

                if i!=1 and nums[i-2]>nums[i]:
                    nums[i] = nums[i-1]

                modified = True

        return True

        # l = len(nums)
        # if l<=2:
        #     return True
        # i = 0
        # while i<l-1:
        #     if nums[i]>nums[i+1]:
        #         break
        #     i+=1

        # j = l-2
        # while j>=0:
        #     if nums[j]>nums[j+1]:
        #         break
        #     j-=1

        # if i<j:
        #     return False
        # elif i==j:
        #     if i==l or i==0:
        #         return True
        #     elif max(nums[i-1],nums[i]) <= nums[j+1]:
        #         return True
        #     else:
        #         return False
        # else:
        #     return True



执行用时为 56 ms 的范例
class Solution:
    def checkPossibility(self, A):
        p=None
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                if p is not None:
                    return False
                else:
                    p=i
        return (p is None or p==0 or p==len(A)-2 or A[p-1]<=A[p+1] or A[p]<=A[p+2])