# leetcode-563-二叉树的坡度.py
# 给定一个二叉树，计算整个树的坡度。

# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

# 整个树的坡度就是其所有节点的坡度之和。

# 示例:

# 输入: 
#          1
#        /   \
#       2     3
# 输出: 1
# 解释: 
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
# 注意:

# 任何子树的结点的和不会超过32位整数的范围。
# 坡度的值不会超过32位整数的范围。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.tiltSum = 0

        def Tilt(root):
            leftSum = 0 if not root.left else Tilt(root.left)
            rightSum  = 0 if not root.right else  Tilt(root.right)

            tmp = abs(leftSum-rightSum)
            self.tiltSum+=tmp

            return root.val+leftSum+rightSum
        Tilt(root)
        return self.tiltSum




执行用时为 68 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=0
        def f(root):
            if not root:
                return 0
            l=f(root.left)
            r=f(root.right)
            self.res+=abs(l-r)
            return l+r+root.val#每个节点将有所有子节点与当前结点的和更换
        f(root)
        return self.res
        