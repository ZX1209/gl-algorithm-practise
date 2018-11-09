# leetcodee-703-数据流中的第K大元素.py
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

# 示例:

# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 说明: 
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。

"""
思路:
简单的排序做吗??
"""
import heapq

class KthLargest:
    # 参考
    def __init__(self,k,nums):
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        self.k = k
        self.nums = nums
    def add(self,val):
        if len(self.nums) == self.k and val<=self.nums[0]:
            return self.nums[0]
        heapq.heappush(self.nums,val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

    # def __init__(self, k, nums):
    #     """
    #     :type k: int
    #     :type nums: List[int]
    #     """
    #     self.nums = sorted(nums,reverse=True)[:k]
    #     self.k = k
        

    # def add(self, val):
    #     """
    #     :type val: int
    #     :rtype: int
    #     """
    #     i = self.k-1
    #     while 0<=i:
    #         if self.nums[i]>=val:
    #             self.nums.insert(i+1,val)
    #             self.nums.pop()
    #             break
    #         i-=1

    #     if i==-1:
    #         self.nums.insert(i+1,val)
    #         self.nums.pop()

    #     return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# 执行用时为 84 ms 的范例
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(self.nums)
        self.k = k
        heapq.heapify(self.nums)
        while self.size > self.k:
            heapq.heappop(self.nums)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.nums, val)
            self.size += 1
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)