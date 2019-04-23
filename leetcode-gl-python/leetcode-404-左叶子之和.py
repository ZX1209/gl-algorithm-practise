# leetcode-404-左叶子之和.py
# 计算给定二叉树的所有左叶子之和。

# 示例：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


"""
思路:
直接,递归下..

可以pop,,不用全遍历.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        # 假设不为空
        nodes = [root]

        ans = 0

        while nodes:
            nextnodes = []
            for node in nodes:
                if node.left:
                    nextnodes.append(node.left)

                    # is left leaf
                    if not node.left.left and not node.left.right:
                        ans += node.left.val

                if node.right:
                    nextnodes.append(node.right)

            nodes = nextnodes

        return ans




执行用时为 24 ms 的范例
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        sum = 0
        nodes = list()
        nodes.append(root)

        while nodes:
            node = nodes.pop()
            if node.left:
                if node.left.left == None and node.left.right == None:
                    sum += node.left.val
                else:
                    nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return sum




