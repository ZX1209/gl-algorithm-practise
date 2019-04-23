# leetcode-18-四数之和.py
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：

# 答案中不可以包含重复的四元组。

# 示例：

# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

"""
思路:
嗯,排序,,剪枝

转换为 twosum
要返回四元组呢

递归?

嗯,确实是范例的算法啊..,,想实现还是不容易啊
"""




class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # 参考

        def n_sum(n, pres, nums, target, results):
            if len(nums) < n or target > nums[-1]*n or target < nums[0]*n:
                return
            if n == 2:
                left = 0
                right = len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == target:
                        results.append(pres+[nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while nums[right] == nums[right+1] and right > left:
                            right -= 1
                    elif nums[left]+nums[right] < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums)-n+1):
                    if i == 0 or nums[i] != nums[i-1]:
                        n_sum(n-1, pres+[nums[i]], nums[i+1:],
                              target-nums[i], results)
        results = []
        n_sum(4, [], nums, target, results)

        return results

        # nums.sort()
        # l = len(nums)
        # ans = []

        # for l1 in range(l):
        #     for l2 in range(l1+1,l):
        #         tmp = target - nums[l1] - nums[l2]

        #         if l2+2<l and nums[l2+1]+nums[l2+2]>tmp:
        #             break

        #         for l3 in range(l2+1,l):
        #             for l4 in range(l3+1,l):
        #                 if nums[l3]+nums[l4]>tmp:
        #                     break
        #                 elif nums[l3]+nums[l4] == tmp:
        #                     if [nums[l1],nums[l2],nums[l3],nums[l4]] not in ans:
        #                         ans.append([nums[l1],nums[l2],nums[l3],nums[l4]])

        # return ans


执行用时为 92 ms 的范例


class Solution:
    def fourSum(self, nums, target):
        """
        method1 112ms 97.93%
        先做排序，选定前两个数后，双指针指向后两个数的可选范围的边界，根据sum与target的关系，移动指针
        trick1: 前两个数在遍历过程中，遇到连续的相同数时跳过
        trick2: 前两个数固定后，将后两个数可选范围内的极值同target比较，极端情况下可以提前终止该轮或者整个循环
        trick3: 每次均求和同target比较计算次数太多，可以事先对target和已确定数做减法替代
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        length = len(nums)

        for i, x in enumerate(nums[:-3]):
            target1 = target - x
            if sum(nums[i:i + 4]) > target:
                break
            elif sum(nums[-3:]) < target1 or (i > 0 and x == nums[i - 1]):
                continue
            for j in range(i + 1, length - 2):
                target2 = target1 - nums[j]
                if nums[j + 1] + nums[j + 2] > target2:
                    break
                elif nums[-2] + nums[-1] < target2 or (j > i + 1 and nums[j] == nums[j - 1]):
                    continue
                k, l = j + 1, length - 1
                while k < l:
                    temp = nums[k] + nums[l]
                    if temp > target2:
                        l -= 1
                    elif temp < target2:
                        k += 1
                    else:
                        res.append([x, nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k, l = k + 1, l - 1
        return res

        # method2
#         def findNsum(nums,target,N,result,results):
#             # early termination
#             if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1]*N:
#                 return

#             # two pointer solve sorted 2-sum problem
#             if N == 2:
#                 l,r = 0, len(nums) - 1
#                 while l < r:
#                     s = nums[l] + nums[r]
#                     if s == target:
#                         results.append(result + [nums[l], nums[r]])
#                         l += 1
#                         while l < r and nums[l] == nums[l-1]:
#                             l += 1
#                     elif s < target:
#                         l += 1
#                     else:
#                         r -= 1

#             # recursively reduce N
#             else:
#                 for i in range(len(nums) - N + 1):
#                     if i == 0 or (i > 0 and nums[i-1] != nums[i]):
#                         findNsum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)

#         results = []
#         findNsum(sorted(nums),target,4,[],results)
#         return results
