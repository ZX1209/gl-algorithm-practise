# leetcode-每个节点的右向指针.py
# 给定一个二叉树

# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。

# 说明:

# 你只能使用额外常数空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
# 示例:

# 给定完美二叉树，

#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# 调用你的函数后，该完美二叉树变为：

#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL


"""
思路:
这个,也只是层次遍历啊..

范例,,用了他的答案来构建它..


"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        nodes = [root] if root else None

        while nodes:
            l = len(nodes)
            tmpnodes = []
            for i in range(0,l-1):
                nodes[i].next = nodes[i+1]

                if nodes[i].left : tmpnodes.append(nodes[i].left)
                if nodes[i].right : tmpnodes.append(nodes[i].right)

            if nodes[l-1].left : tmpnodes.append(nodes[l-1].left)
            if nodes[l-1].right : tmpnodes.append(nodes[l-1].right)
            nodes = tmpnodes



# 执行用时为 48 ms 的范例
# # Definition for binary tree with next pointer.
# # class TreeLinkNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# #         self.next = None

# class Solution:
#     # @param root, a tree link node
#     # @return nothing
#     def connect(self, root):
#         if not root:return
#         pre,cur = root,None
#         while pre.left:
#             cur = pre
#             while cur:
#                 cur.left.next = cur.right
#                 if cur.next:
#                     cur.right.next = cur.next.left
#                 cur = cur.next
#             pre = pre.left
#            