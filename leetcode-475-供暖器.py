# leetcode-475-供暖器.py
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。

# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

# 说明:

# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
# 示例 1:

# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 示例 2:

# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。


"""
思路:
加热半径?,嗯,最大相邻距离的一半??

还要算左右距离.. 默认加一和最后呢.?
不能默认假设呢..

题目中的houses时房子位置.


房屋范围,供暖器范围..  

题目,,没有看透啊..  


房屋范围

供暖器范围..分类??

范例 左右 inf 防止越界..  

关键是houses 啊.. 
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()

        # 全左
        if heaters[-1] <= houses[0]:
            return houses[-1]-heaters[-1]
        # 全右
        elif houses[-1]<= heaters[0]:
            return heaters[0] - houses[0]
        # 偏左
        elif heaters[-1]<=houses[0] and heaters[0]<=houses[0]:
            pass
        # 偏右
        elif heaters[0]<=houses[-1] and heaters[-1] >= houses[-1]:
            pass
        # 中
        elif heaters[0]>=houses[0] and heaters[-1] <= houses[-1]:
            pass
        # 包含
        elif heaters[0]<=houses[0] and heaters[-1] >= houses[-1]


        left = heaters[0]-houses[0]
        right = houses[-1] - heaters[-1]

        tmpmax = max(left,right)

        maxdis = 0

        for i in range(1,len(heaters)):
            if heaters[i]-heaters[i-1] > maxdis:
                maxdis = heaters[i]-heaters[i-1]

        tmp = maxdis//2



        return tmp if tmp>=tmpmax else tmpmax

# 参考
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]

        i = 0
        radius = -1

        for house in houses:
            while heaters[i+1]<house:
                i+=1

            leftDis = house - heaters[i]
            rightDis = heaters[i+1] - house

            closest = min(leftDis,rightDis)
            radius = max(radius,closest)

        return radius

执行用时为 84 ms 的范例
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        heaters = [float('-inf')]+heaters+[float('inf')]
        r = i =0
        for x in sorted(houses):
            while x>heaters[i+1]:
                i+=1
            dis = min(x-heaters[i],heaters[i+1]-x)
            r = max(r,dis)
        return r
