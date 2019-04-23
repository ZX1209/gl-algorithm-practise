# leetcode-111-二叉树的最小深度.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.


"""
思路:
也是dfs
只不过,,可以,很好的优化
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        # 两边都有
        if root.left and root.right:
            return 1+ min(self.minDepth(root.left),self.minDepth(root.right))
        # 有一边有
        elif root.left or root.right:
            return 1+self.minDepth(root.left if root.left else root.right)
        # 两边都没有
        else:
            return 1


# 参考 
# 执行用时为 32 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root == None:
#             return 0
        
#         nodebuf = [root]
#         depth = 2
#         while nodebuf:
#             nextnodebuf = []
#             for node in nodebuf:
#                 if node.left:
#                     nextnodebuf.append(node.left)
#                 if node.right:
#                     nextnodebuf.append(node.right)
#                 if not (node.left or node.right):
#                     return depth - 1
            
#             depth += 1
            
#             nodebuf = nextnodebuf
            
#         return depth - 1