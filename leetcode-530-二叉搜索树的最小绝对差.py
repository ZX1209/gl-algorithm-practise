# leetcode-530-二叉搜索树的最小绝对差.py
# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

# 示例 :

# 输入:

#    1
#     \
#      3
#     /
#    2

# 输出:
# 1

# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 注意: 树中至少有2个节点。


"""
思路:
遍历,从小到大排序,距离.优化
"""

        # if root is None:
        #     return
        # r = []
        # que = [root]
        # while que:
        #     q = que.pop()
        #     r.append(q.val)
        #     if q.left:
        #         que.append(q.left)
        #     if q.right:
        #         que.append(q.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curNodes = [root]
        vals = []

        while curNodes:
            tmpNodes = []
            for node in curNodes:
                vals.append(node.val)

                if node.left:
                    tmpNodes.append(node.left)

                if node.right:
                    tmpNodes.append(node.right)
            curNodes = tmpNodes

        vals.sort()

        l = len(vals)
        mindis = vals[-1]

        for i in range(1,l):
            dis = vals[i]-vals[i-1]

            if dis==0:
                return 0

            if dis<mindis:
                mindis = dis

        return mindis
        
执行用时为 80 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 
        # a=[root.val]
        # b=[root.val]
        # def search(q):
        #     if not q:
        #         return None
        #     if q.left:
        #         a.append(q.left.val)
        #         search(q.left)
        #     if q.right:
        #         b.append(q.right.val)
        #         search(q.right)
        # search(root)
        # print(a)
        # return
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(abs(a - b) for a, b in zip(L, L[1:]))


执行用时为 84 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        r = []
        que = [root]
        while que:
            q = que.pop()
            r.append(q.val)
            if q.left:
                que.append(q.left)
            if q.right:
                que.append(q.right)
        r = sorted(r)
        return min([abs(i-j) for i,j in zip(r[:-1],r[1:])])