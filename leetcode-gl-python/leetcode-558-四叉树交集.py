# leetcode-558-四叉树交集.py
# 四叉树是一种树数据，其中每个结点恰好有四个子结点：topLeft、topRight、bottomLeft 和 bottomRight。四叉树通常被用来划分一个二维空间，递归地将其细分为四个象限或区域。

# 我们希望在四叉树中存储 True/False 信息。四叉树用来表示 N * N 的布尔网格。对于每个结点, 它将被等分成四个孩子结点直到这个区域内的值都是相同的。每个节点都有另外两个布尔属性：isLeaf 和 isLeaf。当这个节点是一个叶子结点时 isLeaf 为真。val 变量储存叶子结点所代表的区域的值。

# 例如，下面是两个四叉树 A 和 B：

# A:
# +-------+-------+   T: true
# |       |       |   F: false
# |   T   |   T   |
# |       |       |
# +-------+-------+
# |       |       |
# |   F   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight: T
# bottomLeft: F
# bottomRight: F

# B:               
# +-------+---+---+
# |       | F | F |
# |   T   +---+---+
# |       | T | T |
# +-------+---+---+
# |       |       |
# |   T   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight:
#      topLeft: F
#      topRight: F
#      bottomLeft: T
#      bottomRight: T
# bottomLeft: T
# bottomRight: F
 

# 你的任务是实现一个函数，该函数根据两个四叉树返回表示这两个四叉树的逻辑或(或并)的四叉树。

# A:                 B:                 C (A or B):
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       | F | F |  |       |       |
# |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
# |       |       |  |       | T | T |  |       |       |
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       |       |  |       |       |
# |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
# |       |       |  |       |       |  |       |       |
# +-------+-------+  +-------+-------+  +-------+-------+
 

# 提示：

# A 和 B 都表示大小为 N * N 的网格。
# N 将确保是 2 的整次幂。
# 如果你想了解更多关于四叉树的知识，你可以参考这个 wiki 页面。
# 逻辑或的定义如下：如果 A 为 True ，或者 B 为 True ，或者 A 和 B 都为 True，则 "A 或 B" 为 True。


"""
思路:
展开来比较??

还要归一回去呢..

闭包更好吗?
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        tmp = Node(None,False,None,None,None,None)

        # 全是叶子
        if quadTree1.isLeaf and quadTree2.isLeaf:
            tmp.isLeaf = True
            tmp.val = quadTree1.val | quadTree2.val
            return tmp
        # 至少 有一个不是叶子
        else:
            if quadTree2.isLeaf:
                if quadTree2.val:
                    tmp.isLeaf = True
                    tmp.val = True
                    return tmp
                quadTree2.isLeaf = False
                quadTree2.topRight = Node(quadTree2.val,True,None,None,None,None)
                quadTree2.topLeft = Node(quadTree2.val,True,None,None,None,None)
                quadTree2.bottomRight = Node(quadTree2.val,True,None,None,None,None)
                quadTree2.bottomLeft = Node(quadTree2.val,True,None,None,None,None)

            if quadTree1.isLeaf:
                if quadTree2.val:
                    tmp.isLeaf = True
                    tmp.val = True
                    return tmp
                quadTree1.isLeaf = False
                quadTree1.topRight = Node(quadTree1.val,True,None,None,None,None)
                quadTree1.topLeft = Node(quadTree1.val,True,None,None,None,None)
                quadTree1.bottomRight = Node(quadTree1.val,True,None,None,None,None)
                quadTree1.bottomLeft = Node(quadTree1.val,True,None,None,None,None)
            tmp.val = False
            tmp.topLeft = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            tmp.topRight = self.intersect(quadTree1.topRight,quadTree2.topRight)
            tmp.bottomRight = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
            tmp.bottomLeft = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)

            # 合并?
            if tmp.topLeft.val and tmp.topRight.val and tmp.bottomLeft.val and tmp.bottomRight.val:
                tmp.isLeaf = True
                tmp.val = True
                tmp.topLeft =None
                tmp.topRight = None
                tmp.bottomRight = None
                tmp.bottomLeft = None


            return tmp

执行用时为 160 ms 的范例
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
 
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        def qd(quadTree1, quadTree2):
            if quadTree1.isLeaf:
                return quadTree1 if quadTree1.val else quadTree2
            else:
                if quadTree2.isLeaf:        
                        return quadTree2 if quadTree2.val else quadTree1
                else:
                    quadTree1.topLeft = qd(quadTree1.topLeft,quadTree2.topLeft)
                    quadTree1.topRight = qd(quadTree1.topRight,quadTree2.topRight)
                    quadTree1.bottomLeft = qd(quadTree1.bottomLeft,quadTree2.bottomLeft)
                    quadTree1.bottomRight = qd(quadTree1.bottomRight,quadTree2.bottomRight)
                    if quadTree1.topLeft.isLeaf and quadTree1.topRight.isLeaf and quadTree1.bottomLeft.isLeaf and quadTree1.bottomRight.isLeaf:
                        if quadTree1.topLeft.val and quadTree1.topRight.val and quadTree1.bottomLeft.val and quadTree1.bottomRight.val:
                            return Node(True,True,None,None,None,None)
                        elif not quadTree1.topLeft.val and not quadTree1.topRight.val and not quadTree1.bottomLeft.val and not quadTree1.bottomRight.val:
                            return Node(False,True,None,None,None,None)
            #quadTree1.val = False
            return quadTree1
        return qd(quadTree1, quadTree2)



