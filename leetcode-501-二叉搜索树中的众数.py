# leetcode-501-二叉搜索树中的众数.py
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

# 假定 BST 有如下定义：

# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 例如：
# 给定 BST [1,null,2,2],

#    1
#     \
#      2
#     /
#    2
# 返回[2].

# 提示：如果众数超过1个，不需考虑输出顺序

# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）


"""
思路:
全遍历一遍?

递归

dic key with max of dic values
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict

class Counter:
    def __init__(self):
        self.tian = [set()]

    def add(self,value):
        end = len(self.tian)-1
        while end>=0:
            if value in self.tian[end]:
                self.tian[end].remove(value)
                break
            end-=1
        try:
            self.tian[end+1].add(value)
        except:
            self.tian.append({value})
    def most_common(self):
        return list(self.tian[-1])

class Solution:
    def __init__(self):
        self.counter  =Counter()

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.counter.add(root.val)
            if root.left: self.findMode(root.left)
            if root.right: self.findMode(root.right)
        else:
            return []

        return self.counter.most_common()

执行用时为 68 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
# from queue import Queue
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        dic = defaultdict(int)
        q = [root]
        while q:
            tmp = []
            for node in q:
                dic[node.val] += 1
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            q = tmp
        max_v = max(dic.values())
        for k, v in dic.items():
            if v == max_v:
                res.append(k)
        return res