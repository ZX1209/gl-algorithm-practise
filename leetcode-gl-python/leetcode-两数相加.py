# leetcode-两数相加.py
# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

"""
思路:
遍历相见喽..


0 的 问题
空 的 问题

.. 
...

..
....

....
..

...
..

关于next 的问题,,还是很难解决啊,,不然,可以挺好的实现的

抓住重点..嗯..

其实参考也想到了..但感觉会超时呢.
没特别规定就试试吗..
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # prev = result = ListNode(None)
        # carry = 0

        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val 
        #         l1 = l1.next

        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next

        #     prev.next = ListNode(carry%10)
        #     prev = prev.next
        #     carry //= 10




        # return result.next


        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val 
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            prev.next = ListNode(carry%10)
            prev = prev.next
            carry //= 10




        return result.next


