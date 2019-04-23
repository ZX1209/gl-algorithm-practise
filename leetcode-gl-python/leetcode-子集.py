# leetcode-子集.py
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

"""
思路:
排列组合??

itertools.combinations...

果然算个数更好点把..

参考1集解答,,用二进制位来表示取的数

参考2使用不重复的,dfs..嗯,,反正解决了重复的问题..滑窗??
"""



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nb_subset = 2**len(nums)
        all_subsets = []

        for subset_nb in range(nb_subset):

            subset = []
            for num in nums:
                if subset_nb % 2 == 1:
                    subset.append(num)
                subset_nb //= 2

            all_subsets.append(subset)

        return all_subsets



if __name__ == '__main__':
    nums = [1,2,3]
    test = Solution()
    r = test.subsets(nums)
    print(r)

# 参考2
# 执行用时为 28 ms 的范例

# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         global out,s
#         s = []
#         out = [[]]
#         def dfs(i):
#             global out,s
          
#             for j in range(i,len(nums)):
                
#                 s.append(nums[j])
                
#                 out.append(s[:])
               
#                 dfs(j+1)
#                 s = s[:len(s)-1]
                
               
#         dfs(0)
     
#         return out
















        # if nums == []:
        #     return [[]]

        # ans = [[],nums]

        # l = len(nums)
        # the_nums = nums

        # def combination(combinalist):
        #     if len(the_nums)<=1:
        #         return None

        #     for num in the_nums:
        #         ans.append(combinalist+[num])

        #         the_nums.remove(num)
        #         combination(combinalist+[num])
        #         the_nums.append(num)

        # combination([])

        # return ans
