# leetcode-941-有效的山脉数组.py
# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]
 

# 示例 1：

# 输入：[2,1]
# 输出：false
# 示例 2：

# 输入：[3,5,5]
# 输出：false
# 示例 3：

# 输入：[0,3,2,1]
# 输出：true
 

# 提示：

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 
#  


"""
思路:
认真读题
"""

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return False
        # i =1
        # l = len(A)-1

        # while i<l:
        #     if A[i-1]>=A[i]:
        #         break
        #     i+=1

        # while i<l:
        #     if A[i-1]<=A[i]:
        #         break
        #     i+=1
        # return i>=l


        left = 0
        right = len(A)-1

        while left<right:
            if A[left]>=A[left+1]:
                break
            left+=1

        if left>=right or left<=0:
            return False

        while left<right:
            if A[right-1]<=A[right]:
                break
            right-=1

        return right==left
