# leetcode-643-子数组最大平均数-I.py
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

# 示例 1:

# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

# 注意:

# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。



class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tmpsum = sum(nums[:k])
        ans = tmpsum

        i = k
        l = len(nums)
        while i<l:
            tmpsum-=nums[i-k]
            tmpsum+=nums[i]

            if tmpsum>ans:
                ans=tmpsum
            i+=1

        return ans/k


if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    test = Solution()
    r = test.findMaxAverage(nums,k)
    print(r)


执行用时为 152 ms 的范例
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if nums is None or len(nums) == 0:
            return 0.0
        length = len(nums)
        if length <= k:
            return sum(nums) / length
        max_v, cur_v = sum(nums[:k]), sum(nums[:k])
        for i in range(k, length):
            pre_v = cur_v
            cur_v = pre_v + nums[i] - nums[i-k]
            if max_v < cur_v:
                max_v = cur_v
        return max_v / k