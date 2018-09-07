# 阅读-题解-leetcode-888-公平的糖果交换.py

# 2018年8月28日  |  278次 预览
# 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。

# 因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

# 返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

# 如果有多个答案，你可以返回其中任何一个。保证答案存在。


# 示例 1：

# 输入：A = [1,1], B = [2,2]
# 输出：[1,2]
# 示例 2：

# 输入：A = [1,2], B = [2,3]
# 输出：[1,2]
# 示例 3：

# 输入：A = [2], B = [1,3]
# 输出：[2,3]
# 示例 4：

# 输入：A = [1,2,5], B = [2,4]
# 输出：[5,4]
 

# 提示：

# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# 保证爱丽丝与鲍勃的糖果总量不同。
# 答案肯定存在。
# 解决方案
# 方法：方程求解
# 思路

# 如果爱丽丝交换糖果 x，她将会期待交换一些特定量的糖果 y 回来。

# 算法

# 设爱丽丝和鲍勃分别总计有 S_A, S_BS
# ​A
# ​​ ,S
# ​B
# ​​  的糖果。

# 如果爱丽丝给了糖果 xx，并且收到了糖果 yy，那么鲍勃收到糖果 xx 并给出糖果 yy。那么，我们一定有

# S_A - x + y = S_B - y + x S
# ​A
# ​​ −x+y=S
# ​B
# ​​ −y+x

# 对于公平的糖果交换。这意味着

# y = x + \frac{S_B - S_A}{2} y=x+
# ​2
# ​
# ​S
# ​B
# ​​ −S
# ​A
# ​​ 
# ​​ 

# 我们的策略很简单。对于爱丽丝拥有的每个糖果 xx，如果鲍勃有糖果 y = x + \frac{S_B - S_A}{2}y=x+
# ​2
# ​
# ​S
# ​B
# ​​ −S
# ​A
# ​​ 
# ​​ ，我们就返回 [x，y]。我们在常量时间内使用集 Set 结构来检查Bob是否拥有所需的糖果 yy。


# 复杂度分析

# 时间复杂度：O(A\text{.length} + B\text{.length})O(A.length+B.length)。

# 空间复杂度：O(B\text{.length})O(B.length)，setB 用去的空间。（通过使用 if 语句，我们可以将其改进到 \min(A\text{.length}, B\text{.length})min(A.length,B.length)。）


# 这是求投影的题目,不是求表面积的题目...
class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]: ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans


if __name__ == '__main__':
    test = Solution()
    print(test.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))