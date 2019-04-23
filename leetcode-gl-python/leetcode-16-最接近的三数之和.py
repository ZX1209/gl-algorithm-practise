# leetcode-16-最接近的三数之和.py
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""
思路:
三数和最接近target?
暴力?

三数和最接近

en,,要如何剪枝的问题吗??
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 参考
        nums.sort()

        closest = float('inf')

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            while j<k:
                triple = nums[i]+nums[j]+nums[k]
                if triple == target:
                    return target

                if abs(triple-target)<abs(closest-target):
                    closest = triple

                if triple-target>0:
                    k-=1
                else:
                    j+=1

        return closest


执行用时为 52 ms 的范例
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # method1
        # 排序后双指针
        # s = sum(nums[:3])
        # cha = abs(s - target)
        # nums.sort()
        # l = len(nums)
        # for i in range(l - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     j, k = i + 1, l - 1
        #     while j < k:
        #         temp = nums[i] + nums[j] + nums[k]
        #         temp1 = abs(temp - target)
        #         if temp == target:
        #             return target
        #         else:
        #             if temp1 < cha:
        #                 s = temp
        #                 cha = temp1
        #             if temp > target:
        #                 k -= 1
        #             else:
        #                 j += 1
        # return s
        
        # method2
        nums.sort()
        l = len(nums)
        s = sum(nums[:3])
        cha = abs(s - target)
        
        for i, num in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, l - 1
            temp1 = num + nums[j] + nums[j + 1]
            temp2 = num + nums[k] + nums[k - 1]
            if  temp1> target:
                temp11 = abs(temp1 - target)
                if  temp11 < cha:
                    s, cha = temp1, temp11
                break
            elif  temp2 < target:
                temp21 = abs(temp2 - target)
                if  temp21 < cha:
                    s, cha = temp2, temp21
                continue
            else:
                while j < k:
                    temp3 = num + nums[j] + nums[k]
                    if temp3 < target:
                        temp31 = abs(temp3 - target)
                        if temp31 < cha:
                            s, cha = temp3, temp31
                        j += 1
                    elif temp3 > target:
                        temp31 = abs(temp3 - target)
                        if temp31 < cha:
                            s, cha = temp3, temp31
                        k -= 1
                    else:
                        return target
        return s
                    
                    
                    
                    
                    