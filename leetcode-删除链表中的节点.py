# leetcode-删除链表中的节点.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmph = head
        pre = None

        while tmph:
            if tmph.val == node.val:
                pre.next = tmph.next
                break
            pre = tmph
            tmph = tmph.next

