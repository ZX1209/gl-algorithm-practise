# leetcode-奇偶链表.py
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:

# 输入: 2->1->3->5->6->4->7->NULL 
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:

# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。


"""
思路:
嗯,,思路基本上一样,,就是各种处理上的事啊..
"""

def printNodes(r):
    while r:
        print(r.val,end="->")
        r = r.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def L2N(L):
    ans = head = ListNode(None)
    for one in L:
        tmpNode = ListNode(one)
        head.next = tmpNode
        head = head.next

    return ans.next




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return head

        ans = head
        pre = oddN = ListNode(None)
        last = None

        while ans != None:            
            if ans.next:
                tmpodd = ans.next

                last = ans

                ans.next = ans.next.next

                tmpodd.next = None
                oddN.next = tmpodd
                oddN = oddN.next

                
            else:
                last = ans

            ans = ans.next

        last.next = pre.next


        return head





if __name__ == '__main__':
    l1 = L2N([1,2,3,4,5])
    test = Solution()
    r = test.oddEvenList(l1)
    i = 0
    while r:
        if i > 10:
            break
        i +=1
        print(r.val,end="->")
        r = r.next


# 参考 
# 执行用时为 36 ms 的范例
# class Solution(object):
#     def oddEvenList(self, head):
#         if head is None:
#             return head
#         odd = head
#         even = head.next
#         if even is None:
#             return head
#         odd_prev = odd
#         even_prev = even
#         even_head = even
#         while even.next is not None:
#             odd = even.next
#             even = odd.next
#             odd_prev.next = odd
#             even_prev.next = even
#             odd_prev = odd
#             even_prev = even
#             if even is None:
#                 break
#         odd.next = even_head
#         if even:
#             even.next = None
#         return head