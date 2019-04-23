# leetcode-160-相交链表.py
# 编写一个程序，找到两个单链表相交的起始节点。

 

# 例如，下面的两个链表：

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# 在节点 c1 开始相交。

 

# 注意：

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""
思路:
这,,先遍历一个,记下值,再遍历另一个.??

我的也对啊..集合和列表的区别???

len_diff 还可以

还有一个不是很明白呢..
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB :
            return None

        savedA,savedB = headA ,headB


        # not so understand
        while headA != headB:
            headA = savedB if not headA else headA.next
            headB = savedA if not headB else headB.next

        return headA


        # s2
        # if not headA or not headB:
        #     return None

        # savedA,savedB = headA,headB
        # len_diff = 0

        # while headA.next:
        #     len_diff += 1
        #     headA = headA.next

        # while headB.next:
        #     len_diff -= 1
        #     headB = headB.next

        # if headA != headB:
        #     return None

        # headA,headB = savedA,savedB

        # while len_diff != 0 :
        #     if len_diff > 0:
        #         headA = headA.next
        #         len_diff -= 1
        #     else:
        #         headB = headB.next
        #         len_diff += 1

        # while headA != headB:
        #     headB = headB.next
        #     headA = headA.next

        # return headA








        # if not (headA and headB):
        #     return None

        # s = []

        # while headA:
        #     s.append(headA)
        #     headA = headA.next

        # while headB:
        #     if headB in s:
        #         return headB
        #     headB = headB.next
        # return None

