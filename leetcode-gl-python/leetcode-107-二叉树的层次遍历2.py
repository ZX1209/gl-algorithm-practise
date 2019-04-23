# leetcode-107-二叉树的层次遍历2.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：

# [
#   [15,7],
#   [9,20],
#   [3]
# ]

"""
思路:
嗯 ,,可以把上次的倒过来

不过,,也可以用递归把...不行吧
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        ans = []
        nodes = [root]

        while nodes != []:
            tmpval = [node.val for node in nodes]
            ans.insert(0, tmpval)

            # update nodes
            tmpnodes = []
            for node in nodes:
                if node.left != None:
                    tmpnodes.append(node.left)

                if node.right != None:
                    tmpnodes.append(node.right)
            nodes = tmpnodes

        return ans


执行用时为 40 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res

        queue = [root]
        while queue and queue[0]:
            level = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level:
                res.append(level)
        return res[::-1]
