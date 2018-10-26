# leetcode-617-合并二叉树.py
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

# 示例 1:

# 输入: 
#     Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# 输出: 
# 合并后的树:
#          3
#         / \
#        4   5
#       / \   \ 
#      5   4   7
# 注意: 合并必须从两个树的根节点开始。

"""
思路:
重叠?
"""

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(t1,t2):
            if not t1 and not t2:
                return None
            else:
                if not t1:t1 = TreeNode(0)
                if not t2:t2 = TreeNode(0)

                t1.val += t2.val

                t1.left = merge(t1.left,t2.left)
                t1.right = merge(t1.right,t2.right)
                return  t1
        root = merge(t1,t2)
        return root


执行用时为 92 ms 的范例
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1

