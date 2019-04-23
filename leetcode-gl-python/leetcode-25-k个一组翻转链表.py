# leetcode-25-k个一组翻转链表.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

# 示例 :

# 给定这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5

# 说明 :

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
思路:
1. 递归的
2. 循环的
    head and tail

"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        HEAD = ListNode(0)
        HEAD.next = head
        cur = head

        tmpnodes = [None]*k
        i = 0

        # rest k
        Head = HEAD
        while cur!=None:
            tmpnodes[i] = cur
            i+=1
            cur = cur.next

            if i>=k:
                # swap case
                for ri in range(k-1,0,-1):
                    tmpnodes[ri].next = tmpnodes[ri-1]

                Head.next = tmpnodes[-1]
                tmpnodes[0].next = cur
                Head = tmpnodes[0]
                i=0


        return HEAD.next






# 执行用时为 52 ms 的范例
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head, k):
        p = head
        for i in range(k):
            p = p.next
            if p is None:
                return None
        p = head.next.next
        last = head.next
        for i in range(k - 1):
            last.next = p.next
            p.next = head.next
            head.next = p
            p = last.next
        return last
        
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head
        last = ListNode(0)
        last.next = head
        p = last
        while p is not None:
            p = self.reverse(p, k)
        return last.next

# 执行用时为 64 ms 的范例
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        # 当前节点
        cur = head
        # 前驱结点
        prev = None
        # 后继结点
        end = ListNode(0)
        
        # 检查是否还需翻转
        count = 0
        check = head
        while count < k and check:
            count += 1
            check = check.next
        
        # 进行翻转，递归实现
        if k > 1 and count == k:
            count = 0
            while count < k and cur:
                end = cur.next
                cur.next = prev
                prev = cur
                cur = end
                count += 1
            if end:
                head.next = self.reverseKGroup(end, k)
            return prev
        
        # 无需翻转，返回头结点
        else:
            return head    