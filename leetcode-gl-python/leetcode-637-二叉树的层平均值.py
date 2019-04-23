# leetcode-637-二叉树的层平均值.py
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

# 示例 1:

# 输入:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 注意：

# 节点值的范围在32位有符号整数范围内。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes = [root] if root else []
        ans = []

        while nodes:
            s = 0
            c = 0
            tmpnodes = []
            for node in nodes:
                s += node.val
                c += 1

                if node.left:
                    tmpnodes.append(node.left)
                if node.right:
                    tmpnodes.append(node.right)


            nodes = tmpnodes
            ans.append(s/c)
        return ans



执行用时为 60 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # from collections import deque
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        stack = []
        stack.append([root])
        res = []
        for level in stack:
            temp, sums = [], 0
            for i in level:
                sums += i.val
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if len(temp):
                stack.append(temp)
            res.append(sums / len(level))
        return res