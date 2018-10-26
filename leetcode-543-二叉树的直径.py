# leetcode-543-二叉树的直径.py
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

# 示例 :
# 给定二叉树

#           1
#          / \
#         2   3
#        / \     
#       4   5    
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

# 注意：两结点之间的路径长度是以它们之间边的数目表示。


"""
思路:
递归??

改造下?

子问题,,递归问题??
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 参考
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.diameter = 0

        def helper(root):
            leftLongest = 0 if not root.left else 1+max(helper(root.left))
            rightLongest = 0 if not root.right else 1+max(helper(root.right))

            self.diameter = max(self.diameter,leftLongest+rightLongest)

            return (leftLongest,rightLongest)

        helper(root)

        return self.diameter


执行用时为 36 ms 的范例
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        dia, _ = self.diaAndDepth(root)
        return dia - 1
        
    def diaAndDepth(self, root):
        if root == None:
            return 0, 0
        
        ldia, ldep = self.diaAndDepth(root.left)
        rdia, rdep = self.diaAndDepth(root.right)
        
        dep = ldep if ldep > rdep else rdep
        dep += 1
        
        dia = ldep + rdep + 1
        if dia < ldia:
            dia = ldia
        if dia < rdia:
            dia = rdia
        
        return dia, dep