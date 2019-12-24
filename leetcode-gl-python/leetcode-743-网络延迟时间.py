# leetcode-743-网络延迟时间.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 有 N 个网络节点，标记为 1 到 N。

# 给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

# 现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

# 注意:

# N 的范围在 [1, 100] 之间。
# K 的范围在 [1, N] 之间。
# times 的长度在 [1, 6000] 之间。
# 所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 1 <= w <= 100。

"""
思路:
记录下走过的点.
最大的遍历时间.
孤立点.

并行搜索
"""

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # 参考
        best_times = [float("inf") for _ in range(N+1)]
        best_times[K] = 0

        network = [ [] for _ in range(N+1) ]
        for u,v,w in times:
            network[u].append((v,w));

        nodes = {n for n in range(1,N+1)}

        while nodes:
            
            best_time = float("inf")
            for node in nodes:
                if best_times[node]<best_time:
                    best_time = best_times[node]
                    next_node = node

            if best_time == float("inf"):
                return -1
            nodes.remove(next_node)

            for nbor,time in network[next_node]:
                best_times[nbor] = min(best_times[nbor],best_time+time)

        return max(best_times[1:])




















        # grid = [[0]*(N+1) for _ in range(N+1)]

        # for time in times:
        #     grid[time[0]][time[1]] = time[2]

        # traveled = set()

        # maxTime = 600000

        # def dfs(node,time):
        #     for tmpNode,tmpTime in  enumerate(grid[node][1:],1):
        #         if tmpTime==0 or tmpNode in traveled:


        # print(grid)

