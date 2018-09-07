# leetcode-88-合并两个有序数组.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

# 说明:

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:

# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]

"""
思路:
首先,做了个插入函数

之后??
比较插入,,毕竟是有序的..

数据清洗!!!!!!!!!!!!!!!


哎,,人家从后往前,,,挺不错啊
"""

class Solution:
    def bubleInsert(self,numlist,index,num,empty_key = 0):
        tmpn = num
        # num can't be 0
        for i in range(index,len(numlist)):
            if tmpn == empty_key:
                break
            else:
                numlist[i],tmpn = tmpn,numlist[i]


    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            nums1[i] = None

        mindex = 0
        for i in range(n):
            while nums1[mindex] != None and nums1[mindex]<nums2[i]:
                mindex += 1

            # below   
            # nums2[i] <= nums1[mindex] or nums1[mindex] == None
            self.bubleInsert(nums1,mindex,nums2[i],empty_key=None)





# 参考
# 执行用时为 36 ms 的范例
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         while m>0 and n >0:
#             if nums1[m-1] >= nums2[n-1]:
#                 nums1[m+n-1] = nums1[m-1]
#                 m = m -1
#             else :
#                 nums1[m+n-1] = nums2[n-1]
#                 n = n-1
#         if n > 0 :
#             nums1[:n] = nums2[:n]