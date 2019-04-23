# leetcode-验证二叉搜索树.py
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:

# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:

# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

"""
思路:
递归验证条件喽

嗯,,果然仔细想想还是最大最小值好啊....
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None or (root.left == None and root.right == None):
            return True

        if root.left != None:
            if not root.val > root.left.val:
                return False

            if root.left.right != None:
                if not root.val > root.left.right.val:
                    return False

                if root.left.right.right != None:
                    if not root.val > root.left.right.right.val:
                        return False

            

        if root.right != None:
            if not root.val < root.right.val:
                return False

            if root.right.left != None:
                if not root.val < root.right.left.val:
                    return False

                if root.right.left.left != None:
                    if not root.val < root.right.left.left.val:
                        return False

            

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    # def isValidL(self, root, maxval):
    #     """
    #     :type root: TreeNode
    #     :type maxval: int
    #     :rtype: bool
    #     """
    #     if root == None or (root.left == None and root.right == None):
    #         return True

    #     if root.left != None:
    #         if not root.left.val < root.val:
    #             return False

    #         if root.left.right != None:
    #             if not root.val > root.left.right.val:
    #             return False

    #     if root.right != None:
    #         if not root.val < root.right.val < maxval:
    #             return False

    #         if root.right.left != None:
    #             if not root.val < root.right.left.val:
    #                 return False

    #     return self.isValidL(root.left, root.val) and self.isValidR(root.right, root.val)

    # def isValidR(self, root, minval):
    #     """
    #     :type root: TreeNode
    #     :type minval: int
    #     :rtype: bool
    #     """

    #     if root == None or (root.left == None and root.right == None):
    #         return True

    #     if root.left != None:
    #         if not minval < root.left.val < root.val:
    #             return False

    #         if root.left.right != None:
    #             if not root.val > root.left.right.val:
    #             return False

    #     if root.right != None:
    #         if not root.val < root.right.val < maxval:
    #             return False

    #         if root.right.left != None:
    #             if not root.val < root.right.left.val:
    #                 return False

    #     return self.isValidL(root.left, root.val) and self.isValidR(root.right, root.val)


# 执行用时为 44 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def ValidBST(self,root,min,max):
#         if (root is None):
#             return True
#         elif (root.val <= min or root.val >= max):
#             return False
#         else:
#             return (self.ValidBST(root.left,min,root.val) and self.ValidBST(root.right,root.val,max))
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.ValidBST(root,-2**62,2**62)