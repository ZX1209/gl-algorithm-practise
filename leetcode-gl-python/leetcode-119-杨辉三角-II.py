# leetcode-119-杨辉三角-II.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 3
# 输出: [1,3,3,1]
# 进阶：

# 你可以优化你的算法到 O(k) 空间复杂度吗？

"""
思路:
这,就是,,组合数了呀..


简单题的参考,,
"""
import math
# c_{m}^{n}
def C(m,n):
    return math.factorial(m)/(math.factorial(n)*math.factorial(m-n))

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]

        ans = [1]

        for i in range(1,rowIndex):
            ans.append(int(C(rowIndex,i)))
        ans.append(1)

        return ans


# 参考
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         ans = [1]
#         for i in range(rowIndex):
#             if i==0:
#                 ans.append(1)
#             else:
#                 new_ans=[1]
#                 for j in range(len(ans)-1):
#                     new_ans.append(ans[j]+ans[j+1])
#                 new_ans.append(1)
#                 ans = new_ans
#         return ans