# leetcode-413-等差数列划分.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

# 例如，以下数列为等差数列:

# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 以下数列不是等差数列。

# 1, 1, 2, 5, 7
 

# 数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

# 如果满足以下条件，则称子数组(P, Q)为等差数组：

# 元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

# 函数要返回数组 A 中所有为等差数组的子数组个数。

 

# 示例:

# A = [1, 2, 3, 4]

# 返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。



"""
思路:
首先,用差数组确定最大级的等差子数组,
再计算每个等差子数组包含多少个小的子数组

假设,等差子数组个数为n
3 个的组合有 n-2 个
n-1 个的组合有 2 个
n 个的组合有 1 个

i 个的 组合 有 n-(i-1)

子数组长度 3 -> n-1
包含子数组长度 n-2 + n-3 ... + 2

n 与 n+1 的 差为
n-2?


3:1
4:2+1
5:3+ 2 + 1

"""


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        if N<=2:
            return 0

        ans = 0
        tmp = 2

        lastd = A[1] - A[0]

        for i in range(2,len(A)):
            curd = A[i] - A[i-1]

            if lastd == curd:
                tmp+=1
                ans += tmp-2
            else:
                lastd = curd
                tmp = 2
        

        return ans

        
# 执行用时为 40 ms 的范例
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        dp=[0]*n
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)