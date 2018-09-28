# leetcode-429-N叉树的层序遍历.py
# 给定一个N叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。


# 例如，给定一个 3叉树 :


# 返回其层序遍历:

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]


# 说明:

# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。


"""
思路:
while 喽

尽然又忘记处理特殊情况了!!!!!!!!!!!
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root==None:
            return []

        roots = [root]
        nodes = []

        while roots:
            nodes.append([one.val for one in roots])

            tmpc = []
            for r in roots:
                for boy in r.children:
                    tmpc.append(boy)

            roots = tmpc

        return nodes



# 执行用时为 120 ms 的范例
# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children
# """
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: Node
#         :rtype: List[List[int]]
#         """

#         if not root:
#             return []

#         levels = []

#         q = [root]
#         while q:
#             new_q = []
#             level = []
#             for node in q:
#                 level.append(node.val)
#                 for child in node.children:
#                     new_q.append(child)
#             levels.append(level)
#             q = new_q
#         return levels