# leetcode-922-按奇偶排序数组-II.py
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

# 你可以返回任何满足上述条件的数组作为答案。

 

# 示例：

# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

# 提示：

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

"""
思路:
奇偶指针
"""

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = len(A)

        ei = 0
        oi = 1

        while ei<l and oi<l:

            while ei<l:
                if A[ei]%2==1:
                    break
                ei+=2

            while oi<l:
                if A[oi]%2==0:
                    break
                oi+=2
            if ei<l and oi<l:
                A[ei],A[oi] = A[oi],A[ei]

            ei+=2
            oi+=2

        return A