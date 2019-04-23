# leetcode-257-二叉树的所有路径.py
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 输入:

#    1
#  /   \
# 2     3
#  \
#   5

# 输出: ["1->2->5", "1->3"]

# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""
思路:
分

特殊值!!!


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathStack(self,root,s):
        if root.left == None and root.right == None:
            return [s+[root.val]]
        else:
            l = []
            r = []
            if root.left:
                l = self.pathStack(root.left,s+[root.val])
            if root.right:
                r = self.pathStack(root.right,s+[root.val])
            return l+r

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []

        ans = self.pathStack(root,[])
        result = []

        for one in ans:
            tmp = [str(single) for single in one]
            result.append("->".join(tmp))

        return result


# 参考 
# 执行用时为 28 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def binaryTreePaths(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         if root == None:
#             return []
#         Result, Path_Stack = [], [(root, '')]
#         while Path_Stack:
#             Current_Node, Path = Path_Stack.pop()
#             if not Current_Node.left and not Current_Node.right:
#                 Result.append(Path + '%s' %(Current_Node.val))
#             if Current_Node.right:
#                 Path_Stack.append((Current_Node.right, Path + '%s->' %(Current_Node.val)))
#             if Current_Node.left:
#                 Path_Stack.append((Current_Node.left, Path + '%s->' %(Current_Node.val)))
#         return Result
#     '''
#         def FindPath(root, Path, Result):
#             if root.left is None and root.right is None:
#                 Path += '%s' %(root.val)
#                 Result.append(Path)
#             if root.left:
#                 FindPath(root.left, Path + '%s->' %(root.val), Result)
#             if root.right:
#                 FindPath(root.right, Path + '%s->' %(root.val), Result)
#         if root == None:
#             return []
#         Result = []
#         FindPath(root, '', Result)
#         return Result
#     '''
