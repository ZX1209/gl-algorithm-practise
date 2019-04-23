# leetcode-中序遍历二叉树.py
# 给定一个二叉树，返回它的中序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


"""
思路:
递归我知道

迭代的话..栈..把..
似乎是队列呢..

不不,,这是中序,,头节点,第二个输出..


太慌张了,,要先想好再做啊啊啊啊啊啊啊

嗯,,表达出自己想到意思...
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            leftvals = []
            rightvals = []
            if root.left:
                leftvals = self.inorderTraversal(root.left)

            if root.right:
                rightvals = self.inorderTraversal(root.right)

            return leftvals + [root.val] + rightvals




# 执行用时为 32 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         stack=[]
#         res=[]
#         current=root
#         while len(stack)>0 or current:
#             while current:
#                 stack.append(current)
#                 current=current.left
#             current=stack[-1]
#             stack.pop()
#             res.append(current.val)
#             current=current.right
#         return res