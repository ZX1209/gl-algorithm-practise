# leetcode-661-图片平滑器.py
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

# 示例 1:

# 输入:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# 输出:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 注意:

# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。


"""
思路:
参考 硬编啊..
"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rl = len(M)
        cl = len(M[0])
        ans = [[0]*cl for i in range(rl)]

        for ri in range(rl):
            for ci in range(cl):

                # scan
                tmpsum = 0
                tmpcount = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0<=ri+i<rl and 0<=ci+j<cl:
                            tmpsum+=M[ri+i][ci+j]
                            tmpcount +=1

                ans[ri][ci] = tmpsum//tmpcount
        return ans

if __name__ == '__main__':
    M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    test = Solution()
    r = test.imageSmoother(M)
    print(r)


执行用时为 384 ms 的范例
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if M is None :
            return

        l1 = len(M)
        l2 = len(M[0])
        res = []

        if M ==[[]] or (l1 == 1 and l2 == 1):
            return M
        if l1 == 1 and l2 >= 2:
            tmp = M[0][0] + M[0][1]
            res.append([tmp//2])
            tmp = M[0][-1] + M[0][-2]
            res[0].append(tmp//2)
            for i in range(1,l2-1):
                tmp = M[0][i-1] + M[0][i] + M[0][i+1]
                res[0].insert(i,tmp//3)
            return res

        if l1 >= 2 and l2 == 1:
            tmp = M[0][0] + M[1][0]
            res.append([tmp // 2])
            tmp = M[-1][0] + M[-2][0]
            res.append([tmp // 2])
            for i in range(1, l1 - 1):
                tmp = M[i-1][0] + M[i][0] + M[i+1][0]
                res.insert(i, [tmp // 3])
            return res

        # 第一行第一个
        t1 = (M[0][0] + M[0][1] + M[1][0] + M[1][1])
        # 第一行最后一个
        t2 = (M[0][-1] + M[0][-2] + M[1][-2] + M[1][-1])
        # 最后一行第一个
        t3 = (M[-1][0] + M[-2][0] + M[-2][1] + M[-1][1])
        # 最后一行最后一个
        t4 = (M[-1][-1] + M[-1][-2] + M[-2][-2] + M[-2][-1])

        # 计算第一行
        pre = t1
        tl = []
        tl.append(t1//4)
        if l2 > 2:
            curr = pre + M[0][2] + M[1][2]
            tl.append(curr//6)
            pre = curr
        for i in range(2,l2-1):
            curr = pre - (M[0][i-2] + M[1][i-2]) + (M[0][i+1] + M[1][i+1])
            pre = curr
            tl.append(curr//6)
        tl.append(t2//4)
        res.append(tl)

        # 计算最后一行
        pre = t3
        tl = []
        tl.append(t3//4)
        if l2 > 2:
            curr = pre + M[-2][2] + M[-1][2]
            tl.append(curr//6)
            pre = curr
        for i in range(2,l2-1):
            curr = pre - (M[-1][i-2] + M[-2][i-2]) + (M[-1][i+1] + M[-2][i+1])
            pre = curr
            tl.append(curr//6)
        tl.append(t4//4)
        endL = tl

        # 计算第一列
        pre = t1
        if l1 > 2:
            curr = pre + M[2][0] + M[2][1]
            res.append([ curr//6 ])
            pre = curr
        for i in range(2,l1-1):
            curr = pre - (M[i-2][0] + M[i-2][1]) + (M[i+1][0] + M[i+1][1])
            pre = curr
            res.append([curr//6])

        # 计算最后一列
        pre = t2
        if l1 > 2:
            curr = pre + M[2][-1] + M[2][-2]
            res[1].append(curr//6)
            pre = curr
        for i in range(2,l1-1):
            curr = pre - (M[i-2][-1] + M[i-2][-2]) + (M[i+1][-1] + M[i+1][-2])
            pre = curr
            res[i].append(curr//6)
        res.append(endL)

        if l1 <= 2 or l2 <= 2:
            return res

        # 计算中间
        pre = t1
        hold = 0
        for i in range(1,l1-1):
            if i != 1:
                pre = pre - (M[i-2][0] + M[i-2][1] + M[i-2][2] + M[i-1][2] + M[i][2])
            pre += M[i+1][0] + M[i+1][1]
            for j in range(1,l2-1):
                if j != 1:
                    curr = pre - (M[i-1][j-2]+M[i][j-2]+M[i+1][j-2]) + M[i-1][j+1]+M[i][j+1]+M[i+1][j+1]
                else:
                    curr = pre + M[i-1][j+1]+M[i][j+1]+M[i+1][j+1]
                    hold = curr
                pre = curr
                res[i].insert(j,curr//9)
            pre = hold
        return res



执行用时为 396 ms 的范例
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(M), len(M[0])
        N = [[0 for j in range(c)] for i in range(r)]
        if r == 1:
            if c == 1:
                return M
            N[0][0] = (M[0][0] + M[0][1]) // 2
            N[0][c-1] = (M[0][c-1] + M[0][c-2]) // 2
            for i in range(1, c-1):
                N[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1]) // 3
            return N
        if c == 1:
            N[0][0] = (M[0][0] + M[1][0]) // 2
            N[r-1][0] = (M[r-1][0] + M[r-2][0]) // 2
            for i in range(1, r-1):
                N[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0]) // 3
            return N
        N[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        N[0][c-1] = (M[0][c-1] + M[0][c-2] + M[1][c-1] + M[1][c-2]) // 4
        N[r-1][0] = (M[r-1][0] + M[r-1][1] + M[r-2][0] + M[r-2][1]) // 4
        N[r-1][c-1] = (M[r-1][c-1] + M[r-1][c-2] + M[r-2][c-1] + M[r-2][c-2]) // 4
        for i in range(1, c-1):
            N[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1] + M[1][i-1] + M[1][i] + M[1][i+1]) // 6
            N[r-1][i] = (M[r-1][i-1] + M[r-1][i] + M[r-1][i+1] + M[r-2][i-1] + M[r-2][i] + M[r-2][i+1]) // 6
        for i in range(1, r-1):
            N[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0] + M[i-1][1] + M[i][1] + M[i+1][1]) // 6
            N[i][c-1] = (M[i-1][c-1] + M[i][c-1] + M[i+1][c-1] + M[i-1][c-2] + M[i][c-2] + M[i+1][c-2]) // 6
        for i in range(1, r-1):
            for j in range(1, c-1):
                N[i][j] = (M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] + M[i][j-1] + M[i][j] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]) // 9
        return N