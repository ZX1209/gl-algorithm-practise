# leetcode-Shuffle an Array.py
# 打乱一个没有重复元素的数组。

# 示例:

# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();

# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();

# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();

"""
思路:
随机数生成已经实现
一开始生成全部序列,,会超时,

只能在线做呢..
while   天哪,,我一直忽略了他呢..

小心使用while

交换,一开始也想到了,,但是,,这样真的可以使概率相同吗??这
"""
import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.raw = nums
        self.l = len(nums)

        # print(self.tmp)
        # print(next(self.random))
        # print(next(self.random))

        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.raw

    def randomgen(self):
        b = 3
        m = 1000
        a = 6
        p = 20
        c = 0
        while True:
            c = (a*p+b)%m
            yield c/m
            p = c
        
    # # not finished
    # def rangeall(self,l):
    #     for one in self.raw:
    #         yield from self.rangeall(l+[one])

    # def dfs(self,s,l): 
    #     if len(s)==1:
    #         yield l+list(s)


    #     for tmps in s:
    #         yield from self.dfs(s-{tmps},l+[tmps])
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # if self.raw == []:
        #     return []
        # else:
        #     return self.tmp[int(next(self.random)*len(self.raw))]

        # tmpset = set([i for i in range(self.l)])
        # tmpans = []

        # while tmpset != {}:
        #     randi = random.randint(0,self.l-1)

        #     if randi in tmpset:
        #         tmpans.append(self.raw[randi])
        #         tmpset.remove(randi)

        # return tmpans

        # 参考
        result = self.raw[:]

        for i in range(self.l):
            swap = random.randint(i,self.l-1)
            result[i],result[swap] = result[swap],result[i]

        return result
 
               


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

nums = [1,3,5,1,7]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
param_3 = obj.shuffle()
print(param_2)
print(param_3)

# 参考
# 去你妹的
# 执行用时为 412 ms 的范例
# class Solution:

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.backup = nums[::]
#         self.array = nums

#     def reset(self):
#         """
#         Resets the array to its original configuration and return it.
#         :rtype: List[int]
#         """
#         self.array = self.backup[::]
#         return self.array
        

#     def shuffle(self):
#         """
#         Returns a random shuffling of the array.
#         :rtype: List[int]
#         """
#         random.shuffle(self.array)
#         return self.array


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.reset()
# # param_2 = obj.shuffle()