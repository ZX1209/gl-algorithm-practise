# leetcode-930-和相同的二元子数组.py
# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

 

# 示例：

# 输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
 

# 提示：

# A.length <= 30000
# 0 <= S <= A.length
# A[i] 为 0 或 1

"""
思路:
遍历
"""


class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        l = len(A)
        start = 0
        end = 0
        count = 0
        tmpcount = 0

        while end<=start and start<l:
            while start<l and tmpcount<S:
                if A[start]:
                    tmpcount+=1
                start+=1


            start+=1
            while start<l and tmpcount==S:
                count+=1
                
                if A[start]:
                    tmpcount+=1
                start+=1

            while end<=start and tmpcount>S:
                if A[end]:
                    tmpcount-=1
                end+=1

        return count




        
