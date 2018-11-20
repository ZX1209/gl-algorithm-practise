# leetcode-939-最小面积矩形.py
# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。

# 如果没有任何矩形，就返回 0。

 

# 示例 1：

# 输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
# 示例 2：

# 输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2
 

# 提示：

# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。



class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xpoints = []
        points.sort()
        ans = float('inf')

        pre = points[0][0]
        i = 0
        xpoints.append([pre])
        for point in points:
            if pre == point[0]:
                xpoints[i].append(point[1])
            else:
                pre = point[0]
                xpoints.append([pre])
                i+=1
                xpoints[i].append(point[1])

        # ismin = 0
        for dis in range(1,len(xpoints)):
            # if ismin:
            #     break
            for i in range(len(xpoints)-dis):
                if len(xpoints[i])<3 or len(xpoints[i+dis])<3:
                    continue
                else:
                    tmpdisX = xpoints[i+dis][0]-xpoints[i][0]
                    # if tmpdisX>ans:
                    #     ismin = 1
                    #     break

                    ll = len(xpoints[i])
                    rl = len(xpoints[i+dis])
                    li =1
                    ri = 1
                    tmpSameY = []
                    while li<ll and ri<rl:
                        if xpoints[i][li]<xpoints[i+dis][ri]:
                            li += 1
                        elif xpoints[i][li]>xpoints[i+dis][ri]:
                            ri+=1
                        else:
                            tmpSameY.append(xpoints[i][li])
                            li+=1
                            ri+=1

                    if len(tmpSameY)>=2:
                        tmpdisY = float('inf')
                        for i in range(len(tmpSameY)-1):
                            tmpdisY = min(tmpdisY,tmpSameY[i+1]-tmpSameY[i])
                        ans = min(ans,tmpdisY*tmpdisX)

        return ans if ans != float('inf') else 0


