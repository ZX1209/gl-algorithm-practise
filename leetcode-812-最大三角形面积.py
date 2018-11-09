# leetcode-812-最大三角形面积.py
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释: 
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。


# 注意:

# 3 <= points.length <= 50.
# 不存在重复的点。
#  -50 <= points[i][j] <= 50.
# 结果误差值在 10^-6 以内都认为是正确答案。

"""
思路:
三角形面积,底乘高

跟一个点的最大距离,
跟一条线的最大距离.

好吧,暴力法

范例有点迷啊..
"""

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        l = len(points)

        largest  =0
        for i in range(l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[k]
                    area = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    largest = max(largest,area)

        return largest







        # points.sort()

        # lefts = []
        # rights = []

        # for i in range(1,len(points)):
        #     if points[i][0]==points[i-1][0]:
        #         lefts.append(points)
        #     else:
        #         break

        # for i in range(len(points)-2,-1,-1):
        #     if points[i][0]==points[i+1][0]:
        #         rights.append(points)
        #     else:
        #         break
        # tmpdis = 0
        # lp = 0
        # rp = 0
        # for right in rights:
        #     for left in lefts:
        #         if tmpdis<abs(right[1]-left[1]):
        #             lp = left
        #             rp = right
        #             tmpdis  = abs(right[1]-left[1])





执行用时为 76 ms 的范例
class Solution:

    def outerTrees(self, points):
        def polar_angle(x0, y0, x1, y1):
            x, y = x1 - x0, y1 - y0
            if x != 0:
                return y / x
            else:
                return 2 ** 31 - 1
            return sign * x / ( x + y)
        def noleft(p0, p1, p2):
            x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
            x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
            return x1 * y2 - x2 * y1 < 0
        if len(points) < 4:
            return points

        x, y = points[0]
        pos = 0
        for k, (i, j) in enumerate(points):
            if i < x or (x == i and j < y):
                x, y = i, j
                pos = k
        points.pop(pos)
        points.sort(key = lambda p: (polar_angle(x, y, p[0], p[1]), y - p[1], p[0] - x))
        # TODO: check
        stack = [[x, y]]
        stack.append(points[0])
        stack.append(points[1])
        for i in range(2, len(points)):
            while noleft(stack[-2], stack[-1], points[i]):
                stack.pop()
            stack.append(points[i])
        return stack
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        points = self.outerTrees(points)
        n = len(points)
        for i in range(n - 2):
            a = points[i]
            for j in range(i + 1, n - 1):
                b = points[j]
                v1 = [b[0] - a[0], b[1] - a[1]]
                for k in range(j + 1, n):
                    c = points[k]
                    v2 = [c[0] - a[0], c[1] - a[1]]
                    area = abs(v2[1]*v1[0] - v1[1]*v2[0])
                    res = area if area > res else res
        return res / 2