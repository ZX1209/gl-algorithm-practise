# leetcode-427-建立四叉树.py
# 我们想要使用一棵四叉树来储存一个 N x N 的布尔值网络。网络中每一格的值只会是真或假。树的根结点代表整个网络。对于每个结点, 它将被分等成四个孩子结点直到这个区域内的值都是相同的.

# 每个结点还有另外两个布尔变量: isLeaf 和 val。isLeaf 当这个节点是一个叶子结点时为真。val 变量储存叶子结点所代表的区域的值。

# 你的任务是使用一个四叉树表示给定的网络。下面的例子将有助于你理解这个问题：

# 给定下面这个8 x 8 网络，我们将这样建立一个对应的四叉树：



# 由上文的定义，它能被这样分割：



 

# 对应的四叉树应该像下面这样，每个结点由一对 (isLeaf, val) 所代表.

# 对于非叶子结点，val 可以是任意的，所以使用 * 代替。



# 提示：

# N 将小于 1000 且确保是 2 的整次幂。
# 如果你想了解更多关于四叉树的知识，你可以参考这个 wiki 页面。


"""
思路:
网格四等分...
n*n 不一定会完整分呢...

递归..各种情况..

直到这个区域内的值都是相同的...看清题目!!!!!!!!

"""




# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        tmp = grid[0][0]
        if all(map(lambda x,tmp=tmp:x==tmp,[col  for rows in grid for col in rows])):
            return Node(bool(grid[0][0]),True,None,None,None,None)
        else:
            # nodes ..
            # if len(grid)<=1 and len(grid[0])<=1:
            #     return Node(bool(grid[0][0]),True,None,None,None,None)

            # if len(grid)<=2 and len(grid[0])<=2:
            #     tmpval = [None,None,None,None]
            #     i = 0
            #     for row in grid:
            #         for col in row:
            #             tmpval[i] = col
            #             i+=1
            #         i = 2

            #     tmpnodes = []
            #     for one in tmpval:
            #         if one != None:
            #             tmpnodes.append(Node(one,True,None,None,None,None))
            #         else:
            #             tmpnodes.append(None)

            #     return Node(True,False,*tmpnodes)

            rl = len(grid)
            cl = len(grid[0])

            # topLeft, topRight, bottomLeft, bottomRight
            # left up
            topLeft = self.construct([ row[:cl//2] for row in grid[:rl//2] ])

            # right down
            bottomRight = self.construct([ row[cl//2:] for row in grid[rl//2:] ])

            # left down
            bottomLeft = self.construct([ row[:cl//2] for row in grid[rl//2:] ])

            # right up
            topRight = self.construct([ row[cl//2:] for row in grid[:rl//2] ])

            return Node(True,False,topLeft, topRight, bottomLeft, bottomRight)



if __name__ == '__main__':
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]

    test = Solution()
    r = test.construct(grid)
    print(r)


# 执行用时为 208 ms 的范例
# """
# # Definition for a QuadTree node.
# class Node(object):
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight
# """
# class Solution(object):
#     def construct(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: Node
#         """
#         def check(a, b, c, d):  # check region formed by (a,b) (c,d) 
#             for i in range(a, c):
#                 for j in range(b, d):
#                     if grid[i][j] != grid[a][b]:
#                         return False, "*"
#             return True, bool(grid[a][b])

#         def build(a, b, c, d):
#             isLeaf, val = check(a, b, c, d)
#             node = Node(val, isLeaf, None, None, None, None)
#             if isLeaf:  # no need to divide if leaf 
#                 return node
#             else:
#                 node.topLeft = build(a, b, (a + c) // 2, (b + d) // 2)
#                 node.topRight = build(a, (b + d) // 2, (a + c) // 2, d)
#                 node.bottomLeft = build((a + c) // 2, b, c, (b + d) // 2)
#                 node.bottomRight = build((a + c) // 2, (b + d) // 2, c, d)
#                 return node

#         return build(0, 0, len(grid), len(grid))