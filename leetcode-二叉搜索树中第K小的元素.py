# leetcode-二叉搜索树中第K小的元素.py
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

# 示例 1:

# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1
# 示例 2:

# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？


"""
思路:
中序遍历??

计数??

闭包??
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSearch(self,root):
        if root and not self.ans:
            if root.left:self.inorderSearch(root.left)

            self.c += 1
            if self.c==self.k:
                self.ans = root.val

            if root.right:self.inorderSearch(root.right)
        else:
            return None


    def kthSmallest(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
            self.k = k 
            self.c = 0
            self.ans = 0

            self.inorderSearch(root)

            return self.ans




# 执行用时为 48 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         # 中序遍历是有序的
#         self.c = 0
#         self.r = None
#         def in_order(root):
#             if not root:
#                 return
#             in_order(root.left)
#             self.c +=1 
#             if self.c == k:
#                 self.r = root.val
#                 return
#             in_order(root.right)
        
#         in_order(root)
#         return self.r
#         