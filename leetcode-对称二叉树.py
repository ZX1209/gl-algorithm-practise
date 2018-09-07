# leetcode-对称二叉树.py
# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:

# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

"""
思路:
对称?
左右子树是否相同
可以,,做个层值列表..

可以,,递归...分左右树吗??
就用递归啊
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, l, r):
        if not l and not r:
            return True

        if not l or not r:
            return False

        if l.val != r.val:
            return False

        return self.isMirror(l.left, r.right) and\
            self.isMirror(r.left, l.right)


# 参考
# 执行用时为 40 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root:
#             return True
#         else:
#             return self.Help(root.left,root.right)
#     def Help(self, L, R):
#         if not L and not R:
#             return True
#         elif L and R and L.val == R.val:
#             return self.Help(L.left,R.right) and self.Help(L.right, R.left)
#         else:
#             return False
#         