# leetcode-31-下一个排列.py
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

"""
思路:
将,最大的,,找到??

左边大于右边?

1 2 3 4
1 2 4 3

1 3 2 4
1 3 4 2

1 4 2 3
1 4 3 2

2 1 3 4 
2 1 4 3
2 3 1 4
2 3 4 1

参考跟我的想法一样啊,,可惜我没有实现出来呢..

reverse 方法
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums)==1:
            return 

        l = len(nums)
        i = l-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1

        if i!=-1:
            j = i+1
            while j<l and nums[j]>nums[i]:
                j+=1
            j-=1
            nums[i],nums[j] = nums[j],nums[i]

        # 搞成升序排列??
        # 偶 原来是差了这点啊
        left = i+1
        right = l-1
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1




















        # l = len(nums)
        # i = l-1 
        # while i>0:
        #     if nums[i-1]<nums[i]:
        #         nums[i-1],nums[i] = nums[i],nums[i-1]
        #         return 
        #     i-=1

        # nums.sort()
        # return 




        # sortedNums = sorted(nums,reverse=True)
        # i = 0
        # l = len(sortedNums)

        # while i<l:
        #     if nums[i] !=  sortedNums[i]:
        #         break
        #     i+=1

        # if i==l:
        #     nums.sort()
        # else:
        #     tmpMax = max(nums[i:])
        #     tmpindex  = nums.index(tmpMax)
        #     nums[tmpindex-1],nums[tmpindex] = nums[tmpindex],nums[tmpindex-1]



# 执行用时为 48 ms 的范例
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None
        n, j = len(nums) - 2, len(nums) - 1
        while n >= 0 and nums[n] >= nums[n+1]:
            n -= 1
        if n == -1:
            nums.reverse()
            return None
        while j > n and nums[j] <= nums[n]:
            j -= 1
        nums[n], nums[j] = nums[j], nums[n]
        a = nums[n+1:]
        nums[n+1:] = a[::-1]
        return None
            