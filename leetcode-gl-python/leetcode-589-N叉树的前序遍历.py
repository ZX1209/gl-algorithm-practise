# leetcode-589-N叉树的前序遍历.py
# 给定一个 N 叉树，返回其节点值的前序遍历。

# 例如，给定一个 3叉树 :

 



 

# 返回其前序遍历: [1,3,5,6,2,4]。

 

# 说明: 递归法很简单，你可以使用迭代法完成此题吗?



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        nodes = [root] if root else []
        ans = []
        while nodes:
            node = nodes.pop()
            ans.append(node.val)
            for child in node.children[::-1]:
                nodes.append(child)

        return ans



执行用时为 112 ms 的范例
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def goAlongLeft(self, root, stack, res):
        while root:
            res.append(root.val)
            if root.children:
                stack.extend(root.children[-1:0:-1])
                root = root.children[0]
            else:
                break
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, res = [], []
        while True:
            self.goAlongLeft(root, stack, res)
            if stack:
                root = stack.pop()
            else:
                break
        return res