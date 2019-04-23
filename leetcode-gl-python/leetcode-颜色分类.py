# leetcode-颜色分类.py
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:

# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：

# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？


"""
思路:
双指针??
1要如何处理呢..

参考方法不错啊..分别计数??.铺场,覆盖??..好东西...
"""


# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         l = len(nums)

#         for i in range(l):
#             print(i)
#             if nums[i]!=0:
#                 j = i+1
#                 while j<l:
#                     if nums[j]==0:
#                         break
#                     j+=1

#                 if j<l:
#                     nums[i],nums[j] = nums[j],nums[i]
#                 else:
#                     break


#         for i in range(l-1,0,-1):
#             print(i)
#             if nums[i]!=2:
#                 j = i-1
#                 while 0<=j:
#                     if nums[j]==2:
#                         break
#                     j-=1

#                 if 0<=j:
#                     nums[i],nums[j] = nums[j],nums[i]
#                 else:
#                     break



# 参考 
# 执行用时为 20 ms 的范例
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       
        i,j,k = -1,-1,-1
        for e in nums:
            if e == 0:
                i += 1
                j += 1
                k += 1
                nums[k] = 2
                nums[j] = 1
                nums[i] = 0
                
                
            if e == 1:
                j += 1
                k += 1
                nums[k] = 2
                nums[j] = 1
                
            if e == 2:
                k += 1
                nums[k] = 2
        return 


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    test = Solution()
    r = test.sortColors(nums)
    print(r)