# leetcode-559-N叉树的最大深度.py
# 给定一个 N 叉树，找到其最大深度。

# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

# 例如，给定一个 3叉树 :

 



 

# 我们应返回其最大深度，3。

# 说明:

# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。


"""
思路:
去掉不用的节点..

一层层往下也可以啊
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        self.maxDep = 0
        def findMaxDepth(node,depth):
            self.maxDep = max(depth,self.maxDep)
            if node.children != []:
                for child in node.children:
                        findMaxDepth(child,depth+1)
            

        findMaxDepth(root,1)
        return self.maxDep


执行用时为 104 ms 的范例
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root==None:
            return 0
        childlist=root.children
        count=1
        while True:
            if len(childlist)==0:
                break
            newlist=[]
            count+=1
            for child in childlist:
                if len(child.children)!=0:
                    newlist.extend(child.children)
            childlist=newlist
        return count
