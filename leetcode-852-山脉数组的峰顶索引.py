# leetcode-852-山脉数组的峰顶索引.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 我们把符合下列属性的数组 A 称作山脉：

# A.length >= 3
# 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

 

# 示例 1：

# 输入：[0,1,0]
# 输出：1
# 示例 2：

# 输入：[0,2,1,0]
# 输出：1
 

# 提示：

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A 是如上定义的山脉



class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # i =1
        # l = len(A)-1
        right = len(A)-1

        while 0<right:
            if A[right-1]<=A[right]:
                break
            right-=1

        return right


执行用时为 36 ms 的范例
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        t = max(A)
        return A.index(t)
        