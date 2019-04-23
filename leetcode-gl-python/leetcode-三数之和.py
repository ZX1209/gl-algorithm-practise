# leetcode-三数之和.py
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


"""
思路:
不能重复...

有人先排序做的..嗯,也行..

依据题目 *创造些规律*

题解,第一位的话,,分了好多种情况呢...
适当分一下也无妨.



"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        i = 0
        while i<len(nums):
            j = i+1
            k = len(nums)-1

            while j<k:
                triple_sum = nums[i]+nums[j]+nums[k]

                if triple_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k-=1

                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                elif triple_sum >0:
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k-=1

                else:
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1

            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1

        return ans



# 参考
# 执行用时为 364 ms 的范例
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         l = len(nums)
#         if l < 3:
#             return []

#         nums.sort()

#         ret = []
#         #三数相同，只能是0
#         if nums.count(0) >= 3:
#             ret.append([0,0,0])

#         #同正、同负，无结果
#         if nums[0] >= 0 or nums[-1] <= 0:
#             return ret

#         #二数相同
#         prev = None
#         doubles = []
#         for x in nums:
#             if prev is not None and prev == x and x not in doubles[-1:]:
#                 doubles.append(x)
#             prev = x

#         for x in doubles:
#             if x == 0:
#                 continue
#             sval = -x*2
#             if sval in nums:
#                 if sval > 0:
#                     ret.append([x, x, sval])
#                 else:
#                     ret.append([sval, x, x])

#         #各不相同
#         nums = list(set(nums))
#         nums.sort()
#         print nums

#         neg_len = abs(nums[0])
#         pos_len = abs(nums[-1])
#         max_len = max(neg_len, pos_len)+1
#         negmaps = [False]*max_len #负数
#         posmaps = [False]*max_len #正数
#         for x in nums:
#             if x < 0:
#                 negmaps[-x] = True
#             elif x > 0:
#                 posmaps[x] = True

#         # 包含0
#         if 0 in nums:
#             for x in xrange(1, max_len):
#                 if negmaps[x] and posmaps[x]:
#                     ret.append([-x, 0, x])

#         # 不包含0
#         sep = None
#         for i in xrange(len(nums)):
#             if nums[i] >= 0:
#                 sep = i
#                 break

#         # 两负一正
#         for i in xrange(sep):
#             for j in xrange(sep-1, i, -1):
#                 sval = -(nums[i]+nums[j])
#                 if sval > pos_len:
#                     break
#                 if posmaps[sval]:
#                     ret.append([nums[i], nums[j], sval])

#         # 两正一负
#         if nums[sep] == 0:
#             sep += 1
#         for i in xrange(sep, len(nums)):
#             if nums[i]*2 > neg_len:
#                 break
#             for j in xrange(i+1, len(nums)):
#                 sval = nums[i]+nums[j]
#                 if sval > neg_len:
#                     break
#                 if negmaps[sval]:
#                     ret.append([-sval, nums[i], nums[j]])

#         return ret