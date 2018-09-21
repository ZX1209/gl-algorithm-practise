# leetcode-235-二叉搜索树的最近公共祖先.py
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# 示例 1:

# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:

# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 说明:

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。


"""
思路:
嗯,,公共祖先,,这,,自己也可以是自己祖先

两个就是后代

两个是比较远的后代

有一个是祖先节点..


搜素树!!!!!!!!!!!!!!!!尽然没有看到????

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left,p,q)

        r = self.lowestCommonAncestor(root.right,p,q)

        if l == None and r == None:
            return None

        if l == None:
            return r
        elif r == None:
            return l
        else:
            return root


# 参考 
# 执行用时为 68 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def search(self, root, x, stack):
#         stack.append(root)
#         if x.val < root.val:
#             self.search(root.left, x, stack) # 一定存在
#         elif root.val < x.val:
#             self.search(root.right, x, stack)
#         else:
#             return
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         s_p, s_q = [], []
#         self.search(root, p, s_p)
#         self.search(root, q, s_q)
#         n = min(len(s_q), len(s_p))
#         for i in range(n):
#             if s_p[i] != s_q[i]:
#                 return s_q[i - 1]
#         return s_q[n-1]