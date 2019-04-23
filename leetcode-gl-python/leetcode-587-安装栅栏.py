# leetcode-587-安装栅栏.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

 

# 示例 1:

# 输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# 输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# 解释:

# 示例 2:

# 输入: [[1,2],[2,2],[4,2]]
# 输出: [[1,2],[2,2],[4,2]]
# 解释:

# 即使树都在一条直线上，你也需要先用绳子包围它们。
 

# 注意:

# 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
# 输入的整数在 0 到 100 之间。
# 花园至少有一棵树。
# 所有树的坐标都是不同的。
# 输入的点没有顺序。输出顺序也没有要求。


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# import math


# 顺正逆负
testCases = [
[[1,0],[1,1]], # 1/4 pi
[[1,0],[1,-1]], # -1/4 pi
[[1,0],[-1,-1]], # - 3/4 pi
[[1,0],[-1,1]] # -4/5 pi 
]


import math

def mold(x,y=None):
    if y==None:
        y = x[1]
        x = x[0]
    return math.sqrt(x**2+y**2)
# no
def vectorAngle_asc(v1,v2):
    a1 = math.atan2(v1[1],v1[0])
    a2 = math.atan2(v2[1],v1[0])

    a1 = a1 if a1>=0 else 2*math.pi+a1

    a2 = a2 if a2>=0 else 2*math.pi+a2

    return a1-a2

def vectorAngle_at(v1,v2):
    angle = math.atan2(v1[1],v1[0]) - math.atan2(v2[1],v2[0])

    if angle > math.pi:
        angle -= 2* math.pi
    elif angle < -math.pi:
        angle += 2*math.pi

    return angle


def angleCos(v1,v2):
    return math.acos((v1[0]*v2[0]+v1[1]*v2[1])/(mold(v1)*mold(v2)))

def angleSin(v1, v2):
    """v1 to v2"""
    return math.asin((v1[0]*v2[1]-v1[1]*v2[0])/(math.sqrt(v1[0]**2+v1[1]**2)*math.sqrt(v2[0]**2+v2[1]**2)))

def vangle(v1, v2):
    """v1 to v2"""
    return math.asin((v1[0]*v2[1]-v1[1]*v2[0])/(math.sqrt(v1[0]**2+v1[1]**2)*math.sqrt(v2[0]**2+v2[1]**2)))



def tunNums_normal(point,points):
    p = [None]*len(points)

    for i in range(len(points)):
        p[i] = [points[i][0]-point[0],points[i][1]-point[1]]
    ans = 0
    angle = vangle(p[0],p[-1])
    ans+=angle

    print(angle/math.pi)
    for i in range(1,len(p)):
        angle = vangle(p[i],p[i-1])
        ans+=angle
        print(angle/math.pi)
    return ans

def tunNums(point,points):
    p = [None]*len(points)

    for i in range(len(points)):
        p[i] = [points[i].x-point.x,points[i].y-point.y]

    ans = 0
    angle = vangle(p[0],p[-1])
    ans+=angle

    # print(angle/math.pi)
    for i in range(1,len(p)):
        angle = vangle(p[i],p[i-1])
        ans+=angle
        # print(angle/math.pi)
    return ans


class Solution:
    def outerTrees(self, points):

        def tunNums(point,points):
            p = [None]*len(points)

            for i in range(len(points)):
                p[i] = [points[i].x-point.x,points[i].y-point.y]
            
            ans = 0
            angle = vangle(p[0],p[-1])
            ans+=angle

            # print(angle/math.pi)
            for i in range(1,len(p)):
                angle = vangle(p[i],p[i-1])
                ans+=angle
                # print(angle/math.pi)
            return ans




        if len(points)>3:
            points.sort(key=lambda x:x.x)

            bpoints = []
            bpoints.append(points[0])
            bpoints.append(points[-1])
            points.pop(0)
            points.pop(-1)

            points.sort(key=lambda x:x.y)

            bpoints.append(points[-1])
            bpoints.insert(points[0])
            points.pop(0)
            points.pop(-1)

            i = 0

            while i<len(points):
                tmp = tunNums(points[i],bpoints)
                if  2* math.pi < tmp > 2* math.pi:
                    bpoints.append(points[i])
                i+=1

            return bpoints



# 参考      
class Solution:
    def outerTrees(self, points):
        if len(points)<3:
            return points

        def slope(a,b):
            return float('inf') if a.x==b.x else b.y-a.y/float(b.x-a.x)

        def cross_product(p):
            v1 = [result[-1].x - result[-2].x,result[-1].y-result[-2].y]
            v2 = [p.x-result[-2].x,p.y -  result[-2].y ]
            return v1[0] * v2[1] - v1[1]*v2[0]

        points.sort(key=lambda x:x.x)

        result = []
        result.append(points[0])
        result.append(points[-1])
        points.pop(0)
        points.pop(-1)

        points.sort(key=lambda x:x.y)

        result.append(points[0])
        result.append(points[-1])
        points.pop(0)
        points.pop(-1)

        for point in points:
            while cross_product(point)<0:
                result.pop()
            result.append(point)

        return result


# 卷包裹
class Solution:
    def outerTrees(self, points):
        points.sort(lambda p:(p.x,p.y))
        start_points = points.pop(0)

        next_point = None
        for point in points:
            if cmp_vector([op,point],[op,next_point]) 


    





