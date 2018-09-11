# leetcode-900-RLE_迭代器.py
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Medium
# 编写一个遍历游程编码序列的迭代器。

# 迭代器由 RLEIterator(int[] A) 初始化，其中 A 是某个序列的游程编码。更具体地，对于所有偶数 i，A[i] 告诉我们在序列中重复非负整数值 A[i + 1] 的次数。

# 迭代器支持一个函数：next(int n)，它耗尽接下来的  n 个元素（n >= 1）并返回以这种方式耗去的最后一个元素。如果没有剩余的元素可供耗尽，则  next 返回 -1 。

# 例如，我们以 A = [3,8,0,9,2,5] 开始，这是序列 [8,8,8,5,5] 的游程编码。这是因为该序列可以读作 “三个零，零个九，两个五”。

 

# 示例：

# 输入：["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
# 输出：[null,8,8,5,-1]
# 解释：
# RLEIterator 由 RLEIterator([3,8,0,9,2,5]) 初始化。
# 这映射到序列 [8,8,8,5,5]。
# 然后调用 RLEIterator.next 4次。

# .next(2) 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。

# .next(1) 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。

# .next(1) 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。

# .next(2) 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
# 但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。
 

# 提示：

# 0 <= A.length <= 1000
# A.length 是偶数。
# 0 <= A[i] <= 10^9
# 每个测试用例最多调用 1000 次 RLEIterator.next(int n)。
# 每次调用 RLEIterator.next(int n) 都有 1 <= n <= 10^9 。


"""
思路:
果然还是根据给出的序列来遍历..方法??
"""

class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.pos = 0
        self.A = A
        self.l = len(A)
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """

        while self.pos < self.l:
            while self.A[self.pos]==0:
                self.pos += 2 


            if self.A[self.pos] >= n:
                self.A[self.pos] -= n
                return self.A[self.pos+1]
            else:
                n -= self.A[self.pos]
                self.pos += 2

        return -1

        

A = [3,8,0,9,2,5] 
n=1
# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator(A)
param_1 = obj.next(6)
print(param_1)
print(obj.pos)