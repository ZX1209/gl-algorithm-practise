# leetcode-983-最低票价.py

# 平均星级：4.18 (17次评分)

# 2019年1月27日  |  733 次预览
# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

# 火车票有三种不同的销售方式：

# 一张为期一天的通行证售价为 costs[0] 美元；
# 一张为期七天的通行证售价为 costs[1] 美元；
# 一张为期三十天的通行证售价为 costs[2] 美元。
# 通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

# 返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

 

# 示例 1：

# 输入：days = [1,4,6,7,8,20], costs = [2,7,15]
# 输出：11
# 解释： 
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
# 在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
# 在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
# 在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
# 你总共花了 $11，并完成了你计划的每一天旅行。
# 示例 2：

# 输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# 输出：17
# 解释：
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
# 在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
# 在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
# 你总共花了 $17，并完成了你计划的每一天旅行。
 

# 提示：

# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days 按顺序严格递增
# costs.length == 3
# 1 <= costs[i] <= 1000
# 解决方案
# 方法一：动态规划（日期变量型）
# 思路与算法

# 某天，如果你不必出行的话，等一等再购买火车票一定更优，如果你需要出行的话，那么就有三种选择：在通行期为 1 天、7 天、30 天中的火车票中选择一张购买。

# 我们可以把这种选择的过程表示成递归的形式，然后使用动态规划解决（记忆话搜索）。我们定义 dp(i) 为能够完成从第 i 天到最后的旅游计划的最小花费。那么，如果你在第 i 天需要出行的话，你的花费为：

# \text{dp}(i) = \min(\text{dp}(i+1) + \text{costs}[0], \text{dp}(i+7) + \text{costs}[1], \text{dp}(i+30) + \text{costs}[2])
# dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])


# 复杂度分析

# 时间复杂度：O(W)O(W)，其中 W = 365W=365 是旅行计划中日期的最大值。

# 空间复杂度：O(W)O(W)。 


# 方法二：动态规划（窗口变量型）
# 思路与算法

# 在 方法一 中，我们只需要在有出行需求的日期购买火车票就可以了。

# 现在，我们令 dp(i) 表示能够完成从 days[i] 到最后的旅行计划的最小花费。如果说 j1 是最大的下标满足 days[j1] < days[i] + 1，j7 是最大的下标满足 days[j7] < days[i] + 7， j30 是最大的下标满足 days[j30] < days[i] + 30，那么就有：

# \text{dp}(i) = \min(\text{dp}(j1) + \text{costs}[0], \text{dp}(j7) + \text{costs}[1], \text{dp}(j30) + \text{costs}[2])
# dp(i)=min(dp(j1)+costs[0],dp(j7)+costs[1],dp(j30)+costs[2])


# 复杂度分析

# 时间复杂度：O(N)O(N)，其中 NN 是旅行计划中不同出行日期的数量。

# 空间复杂度：O(N)O(N)。 


# 状态转换方程


from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)

from functools import lru_cache

class Solution:
    def mincostTickets(self, days, costs):
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i): # How much money to do days[i]+
            if i >= N: return 0

            ans = float('inf')
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)

            return ans

        return dp(0)