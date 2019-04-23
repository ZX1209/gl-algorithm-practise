# leetcode-932-漂亮数组.py
# 对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

# 对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

# 那么数组 A 是漂亮数组。

 

# 给定 N，返回任意漂亮数组 A（保证存在一个）。

 

# 示例 1：

# 输入：4
# 输出：[2,1,4,3]
# 示例 2：

# 输入：5
# 输出：[3,1,2,5,4]
 

# 提示：

# 1 <= N <= 1000

"""
思路:
先找找规律..

swap??
"""

from itertools import permutations,product

class Solution:
    def beautifulArray(self,N):
        """
        :type N: int
        :rtype: List[int]
        """
        ans = list(range(1,N+1))
        flag = 1

        while True:
            flag = 1
            for k in range(N):
                for i,j in product(range(k),range(k,N)):
                    if ans[k]*2 == ans[i]+ans[j]:
                        ans[k],ans[j] = ans[j],ans[k]
                        flag = 0

            if flag:
                return ans






def beautifulArray(N):
        """
        :type N: int
        :rtype: List[int]
        """
        ans = []
        flag = 1
        for poss in permutations(range(1,N+1)):
            flag = 1
            for k in range(N):
                for i,j in product(range(k),range(k,N)):
                    if poss[k]*2 == poss[i]+poss[j]:
                        flag = 0
                        break

                if not flag:
                    break
            if flag:
                ans.append(poss)
        return ans