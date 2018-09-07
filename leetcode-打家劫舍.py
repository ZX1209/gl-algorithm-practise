# leetcode-打家劫舍.py
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:

# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""
思路:
首先,嗯,,不能偷相邻的.要选择..
最好是越一格偷..
先找到最大金额的,偷窃
将偷窃的周围房屋去除,
递归,知道房屋为空,,

嗯,,分开来偷...
分治
[1,1,1,1]
[1,1]
[2,3,2]
[1,1,1]
[1,7,9,4]

空值 返回0
一个值 返回那个值
两个值 返回大的那个值
三个值 有两种组合方案
四个值 有三种组合
五个值 

试试,,正规的动态吧..
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1],nums[0]+nums[2])

        localmax = max(nums)
        localindex = nums.index(localmax)

        self.rob(nums[:localindex-1 if localindex-1>=0 else 0]) + localmax + self.rob(nums[localindex+2:])

        self.rob(nums[:localindex-1 if localindex-1>=0 else 0]) + localmax + self.rob(nums[localindex+2:])


        return self.rob(nums[:localindex-1 if localindex-1>=0 else 0]) + localmax + self.rob(nums[localindex+2:])


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        m1 = sum(nums[i] for i in range(0,l,2))
        m2 = sum(nums[i] for i in range(1,l,2))

        return max(m1,m2)


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.l = len(nums)
        self.note = [-1 for i in range(len(nums))]
        return self.noterob(0)

    def noterob(self,i):
        if i == self.l:
            return 0
        elif i == self.l-1:
            return self.nums[i]
        elif i == self.l-2:
            return max(self.nums[i],self.nums[i+1])
        elif i == self.l-3:
            return max(self.nums[i]+self.nums[i+2],self.nums[i+1])


        if self.note[i]!=-1:
            return self.note[i]
        else:
            self.note[i+2] = self.noterob(i+2)

            self.note[i+3] = self.noterob(i+3)

            self.note[i] = max(self.note[i+2]+self.nums[i],self.note[i+3]+self.nums[i+1])

            return self.note[i]

# 参考
# 执行用时为 36 ms 的范例
# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if (len(nums) == 0):
#             return 0
#         elif (len(nums) == 1):
#             return nums[0]
#         elif (len(nums) == 2):
#             return max(nums[0], nums[1])
#         else:
#             v = [0] * len(nums)
#             v[0] = nums[0]
#             v[1] = max(nums[0], nums[1])
#             for i in range(2, len(nums)):
#                 v[i] = max(v[i - 2] + nums[i], v[i - 1])
#             return v[-1]