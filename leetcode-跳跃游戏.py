# leetcode-跳跃游戏.py
# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个位置。

# 示例 1:

# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:

# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


"""
思路:
嗯..dfs??

注意特殊情况的处理..

self.dfs!!!!!!!!

这个用stack挺好的呢.... 
嗯... 


范例也不错啊.. 从后往前其实也想到过..嗯.没有做吧.. 

番茄时间.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = [0]
        max_reach = -1

        # as chances
        while stack:
            index = stack.pop()

            if index+nums[index]>max_reach:
                if index +nums[index] >= len(nums)-1:
                    return True
                for i in range(index+nums[index],max_reach,-1):
                    stack.append(i)
                max_reach = index + nums[index]

        return False


执行用时为 24 ms 的范例
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mingood = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= mingood:
                mingood = i
     
   
        return mingood == 0










# # failed ??
# class Solution(object):
#     def dfs(self,i):
#         # ans is False
#         if self.note[i]:
#             return self.note[i]
#         else:
#             for step in range(self.nums[i],0,-1):
#                 dfs[]
#             self.note[i] = max()

#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         self.l = len(nums)
#         self.nums = nums
#         self.dfs(0)

#         return self.ans

if __name__ == '__main__':
    # nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    nums = [3,2,1,0,4]
    test = Solution()
    r = test.canJump(nums)
    print(r)