# leetcode-回文链表.py
# 请判断一个链表是否为回文链表。

# 示例 1:

# 输入: 1->2
# 输出: false
# 示例 2:

# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


"""
思路:
1. node为空
2. node 不为空
    1. 121
    2. 1221
    3. 1231
    4. 122122

总的来说,,回文是一个从前往后,一个从后往前看是一样的顺序..

最好,,让一半元素进站,,后面的出去..或者,,直接,,全搞进列表里


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True

        l = []
        while head != None:
            l.append(head.val)
            head = head.next

        return l == l[::-1]

# 参考
# 执行用时为 84 ms 的范例
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head or not head.next:
#             return True
#         tmp_list = []
#         while head:
#             tmp_list.append(head.val)
#             head = head.next
#         l = len(tmp_list)
#         for i in range(l//2):
#             if tmp_list[i] != tmp_list[l-1-i]:
#                 return False
#         return True