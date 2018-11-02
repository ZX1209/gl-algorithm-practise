# leetcode-645-错误的集合.py
# 集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

# 示例 1:

# 输入: nums = [1,2,2,4]
# 输出: [2,3]
# 注意:

# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。


"""
思路:
数组长度可以推导出n

重复,与差..

"""


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {i: 0 for i in range(1, len(nums)+1)}

        for num in nums:
            dic[num] += 1
        i = 0
        ans = [0, 0]
        for k, v in dic.items():
            if v == 2:
                i += 1
                ans[0] = k
            elif v == 0:
                i += 1
                ans[1] = k

            if i >= 2:
                return ans


执行用时为 60 ms 的范例
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sets = set(nums)
        i = (n*(n+1)/2) - sum(sets)
        j = (n*(n+1)/2) - sum(nums)
        return [int(i-j), int(i)]