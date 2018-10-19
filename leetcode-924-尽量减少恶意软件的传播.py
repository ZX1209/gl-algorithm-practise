# leetcode-924-尽量减少恶意软件的传播.py
# 在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。

# 一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

# 我们可以从初始列表中删除一个节点。如果移除这一节点将最小化 M(initial)， 则返回该节点。如果有多个节点满足条件，就返回索引最小的节点。

# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后可能仍然因恶意软件传播而受到感染。

 

# 示例 1：

# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
# 示例 2：

# 输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0
# 示例 3：

# 输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
# 输出：1
 

# 提示：

# 1 < graph.length = graph[0].length <= 300
# 0 <= graph[i][j] == graph[j][i] <= 1
# graph[i][i] = 1
# 1 <= initial.length < graph.length
# 0 <= initial[i] < graph.length

"""
思路:
initial 感染列表
"""

class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        l = len(graph)
        chian = {}
        initial.sort()

        possibles = initial.copy()

        for index in initial:
            for i,v in enumerate(graph[index]):
                if v==1 and i!=index:
                    try:
                        possibles.remove(i)
                    except:
                        continue
        if possibles==[]:
            return initial[0]

        count = []
        print(possibles,initial)

        for possible in possibles:
            count.append((possible,sum(graph[possible])))

        count.sort(key=lambda x:100*x[1]-x[0])
        print(count)

        return count[-1][0]




if __name__ == '__main__':
    graph = [[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,1,1]]

    initial = [3,1]
    test = Solution()       
    r = test.minMalwareSpread(graph,initial)
    # print(r)
[[1,0,0,0,1,0,0,0,0,0],
[0,1,1,0,0,0,0,0,0,0],
[0,1,1,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[1,0,0,0,1,0,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0],
[0,0,0,0,0,0,1,0,0,1],
[0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,1,0,0,1]]
[1,3,0]