# leetcode-963-最小面积矩形-II.py
# 枚举  遍历

# 平均星级：5 (5次评分)

# 2019年2月1日  |  539 次预览
# 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。

# 如果没有任何矩形，就返回 0。

 

# 示例 1：



# 输入：[[1,2],[2,1],[1,0],[0,1]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。
# 示例 2：



# 输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
# 输出：1.00000
# 解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
# 示例 3：



# 输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
# 输出：0
# 解释：没法从这些点中组成任何矩形。
# 示例 4：



# 输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
 

# 提示：

# 1 <= points.length <= 50
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。
# 与真实值误差不超过 10^-5 的答案将视为正确结果。
# 解决方案
# 方法一：枚举三角形
# 思路

# 对于每一个三角形，我们尝试寻找第四个点并判定它们是否能形成一个矩形。

# 算法

# 假设前三个点分别是 p1, p2, p3，并且 p2 与 p3 在最终的矩形中处于对角位置。那么第四个点一定是 p4 = p2 + p3 - p1（向量计算），因为 p1, p2, p4, p3 一定形成一个平行四边形，满足 p1 + (p2 - p1) + (p3 - p1) = p4。

# 如果计算得到的第四个点存在于给定的点集中（我们可以使用一个 HashSet 来判定是否存在），那么接下来我们应该判定平行四边形的某一个角的度数是否为 90 度。最简单的判定方法就是计算向量 (p2 - p1) 与 (p3 - p1) 的点积。（另一种方法是我们把它们都规范化成长度为 1 的向量，然后检查其中一个是否与另一个旋转 90 度相等）


# 复杂度分析

# 时间复杂度：O(N^3)O(N 
# 3
#  )，其中 NN 是点集 points 的大小。

# 空间复杂度：O(N)O(N)。 


# 方法二：枚举中心
# 思路

# 我们可以考虑一个矩形 ABCD 的对角线 AC 与 BD。它们共享同一个中点 O，并且中点到顶点的长度均相同 dist(O, A) == dist(O, B) == dist(O, C) == dist(O, D)。 注意到形成一个矩形的充分必要条件是两条对角线的中点相同且端点到中点距离也相同。

# 由此得到启发，让我们可以将点对 PQ 按照它们的中点 C 与距中点距离 r = dist(P, C) 分类。我们的策略就是暴力枚举属于相同分类的点对。

# 算法

# 对于每一个点对，按照它们的 中点 与 中点距 进行分类。我们只需要记录其中一个点 P 就可以了，因为另一个点可以计算得出 P' = 2 * center - P（向量计算）。

# 对于每对 中点 与 中点距，我们检查每一个可行的矩形（假设两个点对分别为 P, P', Q, Q'）。这个矩形的面积 dist(P, Q) * dist(P, Q') 可作为一个候选答案。


# 复杂度分析

# 时间复杂度：O(N^2 \log N)O(N 
# 2
#  logN)，其中 NN 是点集 points 的大小。可以证明，被分到同一类的点对数量的上界为 \log NlogN - 点击链接查看更多。

# 空间复杂度：O(N^2)O(N 
# 2
#  )。 



class Solution(object):
    def minAreaFreeRect(self, points):
        EPS = 1e-7
        points = set(map(tuple, points))

        ans = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
                v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
                if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                    area = abs(v21) * abs(v31)
                    if area < ans:
                        ans = area

        return ans if ans < float('inf') else 0


class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0