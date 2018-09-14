# leetcode-112-路径总和.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

# 说明: 叶子节点是指没有子节点的节点。

# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


"""
思路:
深搜到子节点,,判断,标记

嗯,,参考直接用主函数了...可以..减sum...可以..

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self,path,root):
        if self.ans:
            return 0

        if not (root.left or root.right):
            if sum(path+[root.val]) == self.sum:
                self.ans = True

        if root.left:
            self.pathSum(path+[root.val],root.left)

        if root.right:
            self.pathSum(path+[root.val],root.right)
        
    def hasPathSum(self, root, tsum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        self.ans = False
        self.sum = tsum

        self.pathSum([],root)

        return self.ans

# 参考
# 执行用时为 36 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def hasPathSum(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: bool
#         """
#         if root==None:
#             return False
#         elif root.left==None and root.right==None:
#             return root.val==sum
#         elif root.left==None:
#             return self.hasPathSum(root.right, sum-root.val)
#         elif root.right==None:
#             return self.hasPathSum(root.left, sum-root.val)
#         else:
#             return self.hasPathSum(root.right, sum-root.val) or self.hasPathSum(root.left, sum-root.val)