# leetcode-23-合并K个排序链表.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 重构列表
        vals = []
        for head in lists:
            while head:
                vals.append(head.val)
                head = head.next

        Head = ListNode(0)
        vals.sort(reverse=True)
        for val in vals:
            tmpNode = ListNode(val)
            tmpNode.next = Head.next
            Head.next = tmpNode

        return Head.next


执行用时为 76 ms 的范例
from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapify(h)
        sorted_head = ListNode(-1)
        cur = sorted_head
        while h:
            (cur_min, index, node) = heappop(h)
            next_node = node.next
            if next_node:
                heappush(h, (next_node.val,index, next_node))
            node.next = None
            cur.next = node
            cur = cur.next
        return sorted_head.next