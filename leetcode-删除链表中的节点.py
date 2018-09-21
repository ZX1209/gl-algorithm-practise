# leetcode-删除链表中的节点.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
思路:
也就直接删啊,,特殊情况还是要处理下的...
"""

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        pre = ans

        while head != None:
            if head.val == val:
                pre.next = head.next

                head = head.next
            else:
                pre = head

                head = head.next

        return ans.next


# 参考
# 执行用时为 60 ms 的范例
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#         if not head:
#             return head
#         result = head
#         while head and head.val == val:
#             result = head.next
#             head = head.next
#         while head:
#             while head.next and head.next.val == val:
#                 head.next = head.next.next
#             head = head.next
#         return result