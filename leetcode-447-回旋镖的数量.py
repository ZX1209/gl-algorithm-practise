# leetcode-447-回旋镖的数量.py
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

# 示例:

# 输入:
# [[0,0],[1,0],[2,0]]

# 输出:
# 2

# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]


"""
思路:
各个对各个的距离.. 

向量..

范例直接算啊啊,,
"""


from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def Sn(a1,an,n,d=None):
            if d!=None:
                n = 1 + (an-a1)/d
                
            return n*(a1+an)/2

        def isEdis(i,j,k):
            dis1 = (i[0]-j[0],i[1]-j[1])
            dis2 = (i[0]-k[0],i[1]-k[1])

            if (dis1[0] == dis2[0] or dis1[0] == -dis2[0]) and (dis1[1] == dis2[1] or dis1[1] == -dis2[1]):
                return True
            else:
                return False
        def vectorminus(v1,v2):
            return (abs(v1[0]-v2[0]),abs(v1[1]-v2[1]))
        def dis(v1,v2):
            return (v1[0]-v2[0])**2+(v1[1]-v2[1])**2

        count = 0
        i = 0
        lp = len(points)

        while i<lp:
            tmp = points[i]
            points.pop(i)
            tmpdis = defaultdict(int)
            for point in points:
                tmpdis[dis(tmp,point)]+=1

            for val in tmpdis.values():
                if val>=2:
                    count += Sn(1,val-1,val-1)
            
            points.insert(i,tmp)

            i+=1


        return 2*count
                


执行用时为 596 ms 的范例
class Solution(object):
    def numberOfBoomerangs(self, points):
        total=0
        for i in range(0,len(points)):
            d={}
            for j in range(0,len(points)):
                l=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                if l in d:
                    total=total+d[l]*2
                    d[l]=d[l]+1
                else:
                    d[l]=1           
        return total