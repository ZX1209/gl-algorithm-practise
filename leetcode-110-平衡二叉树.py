# leetcode-110-平衡二叉树.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:

# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:

# 给定二叉树 [1,2,2,3,3,null,null,4,4]

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。


"""
思路:
这,,dfs喽..

关键事什么??

还是跟参考差那么一点点呢..
除了传数据也可以是状态码,,不冲突就行...
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def treeDeep(self,root):
        if root == None:
            return 0

        leftdeep = self.treeDeep(root.left)
        rightdeep = self.treeDeep(root.right)

        if leftdeep == -1 or rightdeep == -1:
            return -1

        if abs(leftdeep-rightdeep)>1:
            return -1

        return max(self.treeDeep(root.left),self.treeDeep(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.treeDeep(root) != -1


# def stringToTreeNode(input):
#     input = input.strip()
#     input = input[1:-1]
#     if not input:
#         return None

#     inputValues = [s.strip() for s in input.split(',')]
#     root = TreeNode(int(inputValues[0]))
#     nodeQueue = [root]
#     front = 0
#     index = 1
#     while index < len(inputValues):
#         node = nodeQueue[front]
#         front = front + 1

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             leftNumber = int(item)
#             node.left = TreeNode(leftNumber)
#             nodeQueue.append(node.left)

#         if index >= len(inputValues):
#             break

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             rightNumber = int(item)
#             node.right = TreeNode(rightNumber)
#             nodeQueue.append(node.right)
#     return root

# def main():
#     import sys
#     def readlines():
#         for line in sys.stdin:
#             yield line.strip('\n')
#     lines = readlines()
#     while True:
#         try:
#             line = next(lines)
#             root = stringToTreeNode(line)
            
#             ret = Solution().isBalanced(root)

#             out = (ret)
#             print(out)
#         except StopIteration:
#             break

# if __name__ == '__main__':
#     main()