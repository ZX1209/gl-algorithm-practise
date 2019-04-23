# 删除链表的倒数第N个节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = deque(maxlen=n+1)
        thead = ListNode(None)
        thead.next = head
        tmpn = thead
        while tmpn != None:
            nodes.append(tmpn)
            tmpn = tmpn.next

        nodes[0].next = nodes[0].next.next

        if nodes[0].val == None:
            return nodes.next
        else:
            return head

# 执行用时为 40 ms 的范例
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         if head is None:
#             return
        
#         step = 0
#         ptr1 = head
#         ptr2 = head
#         while ptr1 is not None:
#             ptr1 = ptr1.next
#             step += 1
#             if step > n + 1:
#                 ptr2 = ptr2.next
                
#         if step == n:
#             head = head.next
#             return head
        
#         if ptr2.next is not None:
#             ptr2.next = ptr2.next.next
#         return head