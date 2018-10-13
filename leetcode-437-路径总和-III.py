# leetcode-437-路径总和-III.py
# 给定一个二叉树，它的每个结点都存放着一个整数值。

# 找出路径和等于给定数值的路径总数。

# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

# 示例：

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# 返回 3。和等于 8 的路径有:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11


"""
思路:
一层一层??

搜索??

参考,似乎是判断,上面节点的路径和有的个数,然后,看这个总和跟
这个节点差值的个数,就是,这个节点的所有可能形成的和.就这样,递归,求到
所有的..
答案是上浮的..

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict 

class Solution(object):
    def pathSum(self, root, isum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        paths = defaultdict(int)
        paths[0] = 1

        def helper(node, partial):
            if not node:
                return 0

            partial += node.val
            count = paths[partial - isum]
            # print(partial)
            # print(paths)
            # print(count)
            # print('-'*10)

            paths[partial] += 1
            count += helper(node.left,partial)
            count += helper(node.right,partial)
            paths[partial] -=1

            return count

        return helper(root,0)

























        # nodes = [root]
        # vals = [[root.val]]

        # while nodes:
        #     tmpnodes = []

        #     for node in nodes:
        #         if node.left:
        #             tmpnodes.append(node.left)

        #         if node.right:
        #             tmpnodes.append(node.right)
        #     if tmpnodes: vals.append([tmp.val for tmp in tmpnodes])
        #     nodes = tmpnodes

        # self.count = 0

        # def dfs(node,l,e,tsum):
        #     if l>=e:
        #         if tsum==isum:
        #             self.count+=1
        #         return None

        #     for val in vals[l]:
        #         dfs(e,l+1,tsum+val)

        #     return None

        # # 配对数
        # for i in range(1,len(vals)+1):
        #     # 开始标号
        #     for j in range(0,len(vals)-i+1):
        #         dfs(j+i,j,0)



        # return self.count