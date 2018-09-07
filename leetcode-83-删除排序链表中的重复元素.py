# leetcode-83-删除排序链表中的重复元素.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 示例 1:

# 输入: 1->1->2
# 输出: 1->2
# 示例 2:

# 输入: 1->1->2->3->3
# 输出: 1->2->3

"""
思路:
使用集合储存元素,查找重复..
删除的话,,要做前一个节点做呢..
首先第一个元素一定不需要删除

检测是否为空??

简化,,所在的这个一定为不重复元素
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        elements = set()
        tmph = head

        while head.next != None:
            elements.add(head.val)

            while head.next != None and head.next.val in elements:
                head.next = head.next.next 

            head = head.next

            if head == None:
                break

        return tmph


# 执行用时为 48 ms 的范例
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if (not head) or (not head.next):
#             return head
#         first_node = head.next
#         second_node = head
#         while first_node:
            
#             if first_node.val == second_node.val:
#                 first_node = first_node.next
#                 second_node.next = first_node
                
#             else:
#                 first_node =first_node.next
#                 second_node = second_node.next
#         return head