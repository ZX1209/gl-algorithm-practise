# leetcode-897-递增顺序查找树.py
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Easy
# 给定一个二叉树，重新排列树，使树中的最小值现在是树的根结点，并且每个结点没有左子结点，只有一个右子结点。


# 示例 ：

# 输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9

# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9


# 提示：

# 给定树中的结点数介于 1 和 100 之间。
# 每个结点都有一个从 0 到 1000 范围内的唯一整数值。

"""
思路:
可以,,重新造棵树,,不过,,肯定会超时吧..

规整书,,一左一右

aaaaaaaaaaaaa
想复杂了呢.,...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findlast(self, root):
        while root.right != None:
            root = root.right

        return root

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.right != None:
            root.right = self.increasingBST(root.right)

        if root.left != None:
            top = self.increasingBST(root.left)

            last = self.findlast(top)
            root.left = None
            last.right = root
        else:
            top = root

        return top
