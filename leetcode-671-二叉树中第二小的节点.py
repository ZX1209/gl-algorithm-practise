# leetcode-671-二叉树中第二小的节点.py
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 

# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

# 示例 1:

# 输入: 
#     2
#    / \
#   2   5
#      / \
#     5   7

# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 示例 2:

# 输入: 
#     2
#    / \
#   2   2

# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。

"""
思路:
这是可以优化的.呢
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = []
        def dfs(root):
            if not root:
                return None
            self.ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        tmp = sorted(set(self.ans))

        return tmp[1] if len(tmp)>=2 else -1




执行用时为 36 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        first, second = root.val, -1
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val < first:
                first = node.val
            elif first < node.val and (node.val < second or second == -1):
                second = node.val
            if node.left and node.right:
                stack.append(node.right)
                stack.append(node.left)
        return second