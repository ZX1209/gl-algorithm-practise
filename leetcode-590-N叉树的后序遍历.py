# leetcode-590-N叉树的后序遍历.py
# 给定一个 N 叉树，返回其节点值的后序遍历。

# 例如，给定一个 3叉树 :

 



 

# 返回其后序遍历: [5,6,3,2,4,1].

 

# 说明: 递归法很简单，你可以使用迭代法完成此题吗?

"""
思路:
记录式迭代
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 参考
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in node.children:
                stack.append(child)
        print(result)
        return result[::-1]


执行用时为 124 ms 的范例
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res