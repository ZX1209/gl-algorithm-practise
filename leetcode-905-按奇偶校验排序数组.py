# leetcode-905-按奇偶校验排序数组.py
# 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

# 你可以返回满足此条件的任何数组作为答案。

 

# 示例：

# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
 

# 提示：

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

"""
思路:
双指针交换
"""

def isodd(n):
    return n%2

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = len(A)

        i = 0
        j = l-1

        while i<j:
            while i<j:
                if isodd(A[i]):
                    break
                i+=1

            while i<j:
                if not isodd(A[j]):
                    break
                j-=1

            A[i],A[j] = A[j],A[i]

        return A