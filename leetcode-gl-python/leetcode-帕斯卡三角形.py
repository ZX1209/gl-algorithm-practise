# leetcode-帕斯卡三角形.py
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

"""
思路:
这,,模拟??因该 不是的
这个应该是排列组合的数据..


防御式编程
"""

import math
def C(m,n):
    return math.factorial(m)/(math.factorial(n)*math.factorial(m-n))

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        if numRows <= 0:
            return []
        if numRows == 1:
            return ans
        elif numRows>1:
            i = 0
            while i<numRows-1:
                l = len(ans[i])
                ans.append([1]*(l+1))
                for ii in range(0,l-1):
                    ans[i+1][ii+1] = ans[i][ii]+ ans[i][ii+1]

                i+=1

        return ans

# 参考
# 执行用时为 20 ms 的范例
# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         if(numRows==0):
#             return([])
#         if(numRows==1):
#             return([[1]])
        
#         s=[[1]]
#         for i in range(1,numRows):
#             t=[]
#             for j in range(len(s[-1])+1):
#                 if(j==0):
#                     t.append(s[-1][0])
#                 elif(j==len(s[-1])):
#                     t.append(s[-1][-1])
#                 else:
#                     t.append(s[-1][j]+s[-1][j-1])
#             s.append(t)
#         return(s)