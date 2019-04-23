# leetcode-环形链表.py
# 给定一个链表，判断链表中是否有环。

# 进阶：
# 你能否不使用额外空间解决此题？


"""
思路:
判断是否有重复的指向,,记录下指向就行了
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        count = set()

        while head!=None:
            if head not in count:
                count.add(head)
            else:
                return False
            head = head.next

        return True


# 执行用时为 44 ms 的范例
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if head is None or head.next is None:
#             return False

#         fast = head.next
#         slow = head
#         while fast != slow:
#             if fast is None or fast.next is None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True