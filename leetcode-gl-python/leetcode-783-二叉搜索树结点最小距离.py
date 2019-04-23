# leetcode-783-\二叉搜索树结点最小距离.py
# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。

# 示例：

# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。

# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:

#           4
#         /   \
#       2      6
#      / \    
#     1   3  

# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
# 注意：

# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root] if root else []
        vals =[]
        while nodes:
            node = nodes.pop()
            vals.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        vals.sort()

        i = 1
        ans = float('inf')
        while i<len(vals):
            ans = min(ans,vals[i]-vals[i-1])
            i+=1
        return ans



        # ans = float('inf')

        # def dfs(root):
        #     nonlocal ans
        #     if not root.left or not root.right :
        #         return None

        #     l = float('inf')
        #     r = float('inf')
        #     if root.left:
        #         dfs(root.left)
        #         l = root.left.val
        #     if root.right:
        #         dfs(root.right)
        #         r = root.right.val
        #     ans = min(ans,root.val-l,r-root.val)
        #     return None
        # dfs(root)

        # return ans


执行用时为 36 ms 的范例
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getlist(self, root, l):
        if root.left:
            self.getlist(root.left, l)
        l.append(root.val)
        if root.right:
            self.getlist(root.right, l)
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = []
        self.getlist(root, l)
        #l.sort()
        for i in range(1,len(l)):
            l[i-1] = l[i] - l[i-1]
       
        return min(l[:-1])