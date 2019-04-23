# leetcode-896-单调数列.py
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Easy
# 如果数组是单调递增或单调递减的，那么它是单调的。

# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

# 当给定的数组 A 是单调数组时返回 true，否则返回 false。

 

# 示例 1：

# 输入：[1,2,2,3]
# 输出：true
# 示例 2：

# 输入：[6,5,4,4]
# 输出：true
# 示例 3：

# 输入：[1,3,2]
# 输出：false
# 示例 4：

# 输入：[1,2,4,5]
# 输出：true
# 示例 5：

# 输入：[1,1,1]
# 输出：true
 

# 提示：

# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000

"""
思路:n
首先,暴力法可以走一波.
"""

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        isincrease = 1
        isdecrease = 1

        for i in range(1,l):
            if not A[i]>=A[i-1]:
                isincrease = 0
                break

        for i in range(1,l):
            if not A[i]<=A[i-1]:
                isdecrease = 0
                break

        if isincrease or isdecrease:
            return True
        else:
            return False