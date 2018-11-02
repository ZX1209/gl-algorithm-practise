# leetcode-653-两数之和-IV-输入BST.py
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

# 案例 1:

# 输入: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# 输出: True
 

# 案例 2:

# 输入: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 28

# 输出: False

"""
思路:
搜索??遍历?

先放,后放..影响..
"""

from collections import defaultdict
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodes = [root] if root else []
        values = defaultdict(int)
        while nodes:
            node = nodes.pop()
            values[node.val]+=1
            if node.val!=k-node.val and  values[k-node.val]!=0:
                return True

            if node.left:
                nodes.append(node.left)

            if node.right:
                nodes.append(node.right)
        return False




执行用时为 92 ms 的范例

from collections import deque

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        if not root:
            return False

        queue = [root]
        nums = set()
        for node in queue:
            val = node.val
            if k - val in nums:
                return True
            nums.add(val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False