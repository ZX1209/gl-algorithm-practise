# leetcode-581-最短无序连续子数组.py
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 你找到的子数组应是最短的，请输出它的长度。

# 示例 1:

# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 说明 :

# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。

"""
思路:
找到不升序排序的呗..
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = sorted(nums)

        i = 0
        l = len(nums)
        while i<l:
            if ref[i]!=nums[i]:
                break
            i+=1

        j = l-1
        while j>i:
            if ref[j]!=nums[j]:
                break
            j-=1
        
        if j==i:
            return 0
        else:
            return j-i+1






        # l = len(nums)
        # if l<=1:
        #     return 0

        # i = 0
        # tmpmin = min(nums[i+1:])
        # while i<l-1:
        #     if  nums[i]>tmpmin:
        #         break
        #     elif nums[i]==tmpmin:
        #         if i+1<l-1:tmpmin=min(nums[i+1:])
        #     i+=1

        # j = l-1
        # tmpmax = max(nums[:j])
        # while j>i:
        #     if  nums[j]<tmpmax:
        #         break
        #     elif nums[j]==tmpmax:
        #         tmpmax = max(nums[i:j])

        #     j-=1

        # if i>=j:
        #     return 0
        # else:
        #     return j-i+1


执行用时为 76 ms 的范例
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < len(nums) - 1 and nums[start] <= nums[start + 1]:
            start += 1
            
        if start == len(nums) - 1:
            return 0
        
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1
            

        vmin = min(nums[start:(end + 1)])
        vmax = max(nums[start:(end + 1)])
        
        while start >= 0 and nums[start] > vmin:
            start -= 1
        while end <= len(nums) - 1 and nums[end] < vmax:
            end += 1
        return end - start - 1