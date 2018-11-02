# leetcode-687-最长同值路径.py
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

# 注意：两个节点之间的路径长度由它们之间的边数表示。

# 示例 1:

# 输入:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出:

# 2
# 示例 2:

# 输入:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出:

# 2
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
思路:
传出两个值,left 和 right 可以


往上回的时候并不能回局部最优,,只能回侧边最优呢..

去,回..
"""

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 参考
        self.longest = 0

        def helper(node):
            if not node:
                return 0,0

            max_left = max(helper(node.left))
            max_right = max(helper(node.right))

            left = 1 + max_left if node.left and node.left.val == node.val else 0

            right = 1 + max_right if node.right and node.right.val == node.val else 0

            self.longest = max(self.longest,left+right)

            return left,right

        helper(root)

        return self.longest






执行用时为 456 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = 0
        
        def helper (root, father):
            if not root:
                return 0

            l = helper(root.left, root.val)
            r = helper(root.right, root.val)
            
            # 更新经过当前结点的相同值路径
            nonlocal longest
            if l+r > longest: 
                longest = l+r

            if root.val == father:
                return max(l, r) + 1
            else:
                return 0
        helper(root, float('-inf'))
        
        return longest











        # self.ans = 0
        # def dfs(root):
        #     if not root:
        #         return 0

        #     tmp = 0
        #     tmpl = 0
        #     tmpr = 0
        #     if root.left:
        #         if root.left.val == root.val:
        #             tmp = tmp+dfs(root.left)+1
        #         else:
        #             tmpl = dfs(root.left)

        #     if root.right:
        #         if root.right.val == root.val:
        #             tmp = tmp+dfs(root.right)+1
        #         else:
        #             tmpr = dfs(root.right)
        #     self.ans = max(self.ans,tmpr,tmpl,tmp)

        #     return tmp

        # dfs(root)

        # return self.ans





        
