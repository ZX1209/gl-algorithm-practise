# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mergel = ListNode(0)
        ans = mergel

        while l1 != None or l2 != None:
            if l1 == None:
                mergel.next = l2
                mergel = mergel.next
                break

            if l2 == None:
                mergel.next = l1
                mergel = mergel.next
                break

            if l2.val <= l1.val:
                mergel.next = ListNode(l2.val)
                mergel = mergel.next
                l2 = l2.next
            else:
                mergel.next = ListNode(l1.val)
                mergel = mergel.next
                l1 = l1.next

        return ans.next


# if __name__ == '__main__':

#     ln1 = ListNode(1)
#     l1 = ln1
#     ln1.next = ListNode(2)
#     ln1 = ln1.next
#     ln1.next = ListNode(4)


#     ln2 = ListNode(1)
#     l2 = ln2
#     ln2.next =  ListNode(3)
#     ln2 = ln2.next
#     ln2.next = ListNode(4)
#     ln2 = ln2.next

#     test = Solution()
#     test.mergeTwoLists(l1,l2)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l2 == None:
#             return l1
#         if l1 == None:
#             return l2
#         result = ListNode(0)
#         result1 = result
#         while l1 and l2:
#             if l1.val >= l2.val:
#                 result1.next = l2
#                 l2 = l2.next
#             else:
#                 result1.next = l1
#                 l1 = l1.next
#             result1 = result1.next
#         while l1:
#             result1.next = l1
#             l1 = l1.next
#             result1 = result1.next
#         while l2:
#             result1.next = l2
#             l2 = l2.next
#             result1 = result1.next
#         return result.next