# leetcode-反转链表.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rhead = ListNode(None)
        while head != None:
            tmpnode = ListNode(head.val)
            tmpnode.next = rhead.next
            rhead.next = tmpnode

            head = head.next

        return rhead.next

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head != None:
            tmpnext = head.next
            head.next = pre
            pre = head
            head = tmpnext

        return pre


# 原地反
# 执行用时为 40 ms 的范例
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         prev = None
#         curr = head
#         while curr:
#             nextTemp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextTemp
#         return prev