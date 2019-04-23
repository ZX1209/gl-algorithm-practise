# leetcode-从前序与中序遍历序列构造二叉树.py
# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7


"""
思路:

递归,,啊啊 好久才想到,,明明以前做过..


范例跟我思路一样,只是做了点优化,,表达没我清晰啊..
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        l = len(inorder)-1
        if l<0:
            return None
        elif l==0:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        

        rootval = preorder[0]
        rindex = inorder.index(rootval)

        leftlen = rindex - 0
        rightlen = l - rindex

        if leftlen>0:
            root.left = self.buildTree(preorder[1:1+leftlen],inorder[:rindex])

        if rightlen>0:
            root.right = self.buildTree(preorder[1+leftlen:],inorder[rindex+1:])

        return root



# 执行用时为 40 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         preorder_l = len(preorder)
#         inorder_dict = dict(zip(inorder, xrange(preorder_l)))

#         if not preorder:
#             return None

#         return self.recursve_build(
#             preorder, 0, preorder_l-1,
#             inorder, 0, preorder_l-1,
#             inorder_dict)
    
#     def recursve_build(
#             self, preorder, p_start, p_end,
#             inorder, i_start, i_end, pos_dict):
#         # Empty tree
#         if p_start > p_end:
#             return None
#         if p_start == p_end:
#             return TreeNode(preorder[p_start])
#         root_val = preorder[p_start]
#         root = TreeNode(root_val)
        
#         # Get the left and right part of inorder
#         inorder_pos = pos_dict[root_val]
#         left_i_start = i_start
#         left_i_end = inorder_pos - 1
#         right_i_start = inorder_pos + 1
#         right_i_end = i_end

#         # Get the left and right part of preorder
#         p_len = left_i_end - left_i_start
#         left_p_start = p_start + 1
#         left_p_end = left_p_start + p_len
#         right_p_start = left_p_end + 1
#         right_p_end = p_end
        
#          # Get the left and right childrens
#         root.left = self.recursve_build(
#             preorder, left_p_start, left_p_end,
#             inorder, left_i_start, left_i_end,
#             pos_dict)
#         root.right = self.recursve_build(
#             preorder, right_p_start, right_p_end,
#             inorder, right_i_start, right_i_end,
#             pos_dict)

#         return root