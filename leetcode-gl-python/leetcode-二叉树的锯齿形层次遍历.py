# leetcode-二叉树的锯齿形层次遍历.py
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]


"""
思路:
首先,,这是一个层次遍历...

锯齿状的话..

先顺序加,,之后,处理..

可以,,减少变脸处理..或者说在一个简单的例子上操作..
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        nodes = [root]
        ans = []
        order = 1

        while nodes:
            nlevel = []

            tmpans = []
            for node in nodes[::order]:
                tmpans.append(node.val)
            ans.append(tmpans)
            order = 0-order

            for node in nodes:
                if node.left: nlevel.append(node.left)
                if node.right: nlevel.append(node.right)

            nodes = nlevel

        return ans


# 执行用时为 24 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if root == None:
#             return []
        
#         result = []
#         nodebuf = [root]
#         flag = 1
#         while nodebuf:
#             if flag == 1:
#                 result.append([node.val for node in nodebuf])
#             else:
#                 result.append([node.val for node in nodebuf[::-1]])
#             nextnodebuf = []
#             for node in nodebuf:
#                 if node.left:
#                     nextnodebuf.append(node.left)
#                 if node.right:
#                     nextnodebuf.append(node.right)
            
#             nodebuf = nextnodebuf
#             flag = -flag
            
#         return result