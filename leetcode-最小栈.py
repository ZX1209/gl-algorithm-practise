# leetcode-最小栈.py
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

"""
思路:
双栈???

常数时间肯定要用..

试试heapq

参考,,将前一个最小与下一个最小联系了起来呢..
组成了一个带有最小信息的栈呢..妙啊..
"""
import heapq
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack != []:
            return self.stack[-1]
        else:
            return -1
        

    def getMin(self):
        """
        :rtype: int
        """
        return heapq.nsmallest(1,self.stack)[0]
        


# Your MinStack object will be instantiated and called as such:
x = 10
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

# 参考
# 执行用时为 56 ms 的范例
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.min = 2147483647
#         self.stack = []

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         if x <= self.min:
#             self.stack.append(self.min)
#             self.min = x
#         self.stack.append(x)

#     def pop(self):
#         """
#         :rtype: void
#         """
#         peak = self.stack.pop()
#         if peak == self.min:
#             self.min = self.stack.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()