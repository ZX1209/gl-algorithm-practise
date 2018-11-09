# leetcode-697-数组的度.py
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

# 示例 1:

# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释: 
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 示例 2:

# 输入: [1,2,2,3,1,4,2]
# 输出: 6
# 注意:

# nums.length 在1到50,000区间范围内。
# nums[i] 是一个在0到49,999范围内的整数。


"""
思路:
频数据
域数据
"""

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmpmax = 0
        dic = {}
        for i,num in enumerate(nums):
            if num in dic:
                dic[num][1] = i
                dic[num][2]+=1
            else:
                dic[num] = [i,i,1]

            if tmpmax<dic[num][2]:
                    tmpmax = dic[num][2]

        tmpmin = len(nums)
        for info in dic.values():
            if info[2]==tmpmax:
                tmpmin = min(tmpmin,info[1]-info[0]+1)

        return tmpmin


# 执行用时为 56 ms 的范例
from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        sorted_c = sorted(c.items(), key=lambda item:item[1], reverse=True)
        key, v = sorted_c[0][0], sorted_c[0][1]
        if v == 1:
            return 1
        start, end = nums.index(key), len(nums)-1-nums[::-1].index(key)
        res = end-start+1
        for item in sorted_c[1:]:
            if item[1] == v:
                start, end = nums.index(item[0]), len(nums)-1-nums[::-1].index(item[0])
                if end-start+1 < res:
                    res = end - start + 1
            else:
                break
        return res