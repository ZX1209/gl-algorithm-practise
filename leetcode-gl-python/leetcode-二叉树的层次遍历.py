# leetcode-二叉树的层次遍历.py
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]
"""
思路:
嗯,,
递归?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
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
            ans.append(tmpval)

            # update nodes
            tmpnodes = []
            for node in nodes:
                if node.left != None:
                    tmpnodes.append(node.left)

                if node.right != None:
                    tmpnodes.append(node.right)
            nodes = tmpnodes

        return ans


# 参考
# 执行用时为 40 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if root == None:
#             return []
#         stack = {0: [root]}
#         ind = 0
#         result = []
#         while len(stack) != 0:
#             last_level = stack.pop(ind)
#             current_level_val = []
#             ind = ind + 1
#             stack[ind] = []
#             flag = False
#             for node in last_level:
#                 current_level_val.append(node.val)
#                 if node.left:
#                     stack[ind].append(node.left)
#                     flag = True
#                 if node.right:
#                     stack[ind].append(node.right)
#                     flag = True
#             if not flag:
#                 stack.pop(ind)
#             result.append(current_level_val)
#         return result