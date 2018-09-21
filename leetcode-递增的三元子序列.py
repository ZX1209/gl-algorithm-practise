# leetcode-递增的三元子序列.py
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

# 数学表达式如下:

# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

# 示例 1:

# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:

# 输入: [5,4,3,2,1]
# 输出: false


"""
思路:
遍历的话,比较慢

还是先排个序


参考,,前后个和后一个的艺术..

if else 的 活用

"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)

        if all(nums[i-1]>=nums[i] for i in range(l-1,0,-1)):
            return False


        tmpn = []
        
        for i,v in enumerate(nums):
            tmpn.append((v,i))

        tmpn.sort()


        i = 0
        while i<=l-3:

            # 遍历 j 第二个
            j = i 
            while j<=l-2:
                if tmpn[j][0]>tmpn[i][0] and tmpn[j][1]>tmpn[i][1]:
                    # 遍历 k 第三个
                    k = j 
                    while k<=l-1:
                        if tmpn[k][0]>tmpn[j][0] and tmpn[k][1]>tmpn[j][1]:
                            return True
                        k += 1
                j += 1

            i += 1

        return False

if __name__ == '__main__':
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    test = Solution()
    r = test.increasingTriplet(nums)
    print(r)



# 参考 
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         a=b=None
#         for n in nums:
#             if a is None or a>=n:
#                 a=n
#             elif b is None or b>=n:
#                 b=n
#             else:
#                 return True
#         return False


# 参考2
# 执行用时为 20 ms 的范例
# class Solution(object):
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) < 3:
#             return False
#         '''
#         # 
#         # 最长递增子序列: time limit exceeded
#         dp = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         print dp
#         return max(dp) >= 3
#         '''
        
#         first = second = float('inf')
#         for n in nums:
#             if n <= first:
#                 first = n
#             elif n <= second:
#                 second = n
#             else:
#                 return True
#         return False