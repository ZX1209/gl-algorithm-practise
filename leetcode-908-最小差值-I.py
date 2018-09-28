# leetcode-908-最小差值-I.py
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。

# 在此过程之后，我们得到一些数组 B。

# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

 

# 示例 1：

# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
# 示例 2：

# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
# 示例 3：

# 输入：A = [1,3,6], K = 3
# 输出：0
# 解释：B = [3,3,3] 或 B = [4,4,4]
 

# 提示：

# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000



class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        minv = min(A)
        maxv = max(A)

        if (maxv-K)>(minv+K):
            return (maxv-K)-(minv+K)
        else:
            return 0