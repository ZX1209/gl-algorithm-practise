# leetcode-538-把二叉搜索树转换为累加树.py
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

# 例如：

# 输入: 二叉搜索树:
#               5
#             /   \
#            2     13

# 输出: 转换为累加树:
#              18
#             /   \
#           20     13


"""
思路:
先遍历个值,递归改值..

累加映射


a二叉搜索啊啊啊啊
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        q = [root] if root else []
        vals = []
        while q:
            curNode = q.pop()
            vals.append(curNode.val)

            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)

        vals.sort(reverse=True)
        l = len(vals)

        sumvals = vals.copy()
        i = 1
        while i < l:
            sumvals[i] += sumvals[i-1]
            i += 1

        dic = {vals[i]: sumvals[i] for i in range(l)}

        q = [root] if root else []
        while q:
            curNode = q.pop()
            curNode.val = dic[curNode.val]

            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)

        return root


执行用时为 92 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.s=0
        def f(root):
            if not root:
                return 
            f(root.right)
            root.val+=self.s
            self.s=root.val
            f(root.left)
        f(root)
        return root