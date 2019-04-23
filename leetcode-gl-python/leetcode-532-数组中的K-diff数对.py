# leetcode-532-数组中的K-diff数对.py
# 给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

# 示例 1:

# 输入: [3, 1, 4, 1, 5], k = 2
# 输出: 2
# 解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
# 示例 2:

# 输入:[1, 2, 3, 4, 5], k = 1
# 输出: 4
# 解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
# 示例 3:

# 输入: [1, 3, 1, 5, 4], k = 0
# 输出: 1
# 解释: 数组中只有一个 0-diff 数对，(1, 1)。
# 注意:

# 数对 (i, j) 和数对 (j, i) 被算作同一数对。
# 数组的长度不超过10,000。
# 所有输入的整数的范围在 [-1e7, 1e7]。

"""
思路:
字典对

k=0 时相同对要怎么办

同一个数包含在两个对中怎么办

start set

集合,,嗯,,有点接近范例了呢..
"""

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        if l<=0:
            return 0

        nums.sort()
        startSet = set()
        count = 0

        i = 0 
        while i<l-1:
            j = i+1
            target = k + nums[i]
            while j<l-1 and nums[j]<target:
                j+=1


            if nums[j]-nums[i]==k:
                if nums[i] not in startSet:
                    count+=1
                    startSet.add(nums[i])
            i+=1

        return count




if __name__ == '__main__':
    nums = [-1,-2,-3]
    k = 1
    test = Solution()
    r = test.findPairs(nums,k)
    print(r)

        
执行用时为 52 ms 的范例
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0
