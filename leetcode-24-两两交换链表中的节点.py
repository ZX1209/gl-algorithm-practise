# leetcode-24-两两交换链表中的节点.py
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 示例:

# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 说明:

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


"""
思路:
实际的进行节点交换吗..

确保此节点后面有有效节点.

优化为迭代
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next:
            left = head
            right = head.next
            left.next = right.next
            right.next = left

            left.next = self.swapPairs(left.next)
            return right

        return head

执行用时为 36 ms 的范例
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        fake_head.next = head
        prev = fake_head

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        return fake_head.next