# leetcode-将有序数组转换为二叉搜索树.py
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定有序数组: [-10,-3,0,5,9],

# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

"""
思路
当然是递归的做了
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None

        if l == 1:
            return TreeNode(nums[0])
        if l == 2:
            tmpn = TreeNode(nums[0])
            tmpn.right = TreeNode(nums[1])
            return tmpn

        mid = int(l/2)
        tmp = TreeNode(nums[mid])

        tmp.left = self.sortedArrayToBST(nums[:mid])
        tmp.right = self.sortedArrayToBST(nums[mid+1:])

        return tmp


if __name__ == '__main__':
    test = Solution()
    test.sortedArrayToBST([-10, -3, 0, 5, 9])


# 参考
# 执行用时为 64 ms 的范例
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         if not nums:
#             return None

#         def insert(nums, l, r):
#             m = (l+r) // 2
#             newNode = TreeNode(nums[m])
#             if l < m:
#                 newNode.left = insert(nums, l, m-1)
#             if r > m:
#                 newNode.right = insert(nums, m+1, r)
#             return newNode

#         return insert(nums, 0, len(nums)-1)
