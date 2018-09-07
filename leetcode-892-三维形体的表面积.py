# leetcode-892-三维形体的表面积.py
# class Solution:
#     def surfaceArea(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         ans = 0

#         l = len(grid)
#         maxtop = [0 for _ in range(l)]
#         maxleft = [0 for _ in range(l)]

#         dis = 0

#         for i in range(l):
#             for j in range(l):
#                 maxleft[i] = max(maxleft[i],grid[i][j])
#                 maxtop[j] = max(maxtop[j],grid[i][j])

#                 if grid[i][j]>0:
#                     ans+=1
#                 else:
#                     if 0<i<l-1 and 0<i<l-1:
#                         dis += 4


#         return 2*(ans+sum(maxleft)+sum(maxtop)) + dis

# 假设,我们只考虑一维的事
# 111 101 111 之类的,,要算他的侧面积...
# 嗯..好像不是很好呢..
#
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0

        l = len(grid)
        maxtop = [0 for _ in range(l)]
        maxleft = [0 for _ in range(l)]

        dis = 0

        for i in range(l):
            for j in range(l):
                if grid[i][j] > 0:
                    ans += 1
                else:
                    if 0 < i < l-1 and 0 < i < l-1:
                        dis += 4

        return 2*(ans+sum(maxleft)+sum(maxtop)) + dis
