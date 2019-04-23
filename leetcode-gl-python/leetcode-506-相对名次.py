# leetcode-506-相对名次.py
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

# (注：分数越高的选手，排名越靠前。)

# 示例 1:

# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
# 提示:

# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。

"""
思路:
排序?

范例才叫映射啊..
"""

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        snums = sorted(nums,reverse=True)

        l = len(snums)
        awards = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        i = 0

        while i<l and i<3:
            nums[nums.index(snums[i])] = awards[i]
            i+=1

        while i<l:
            nums[nums.index(snums[i])] = str(i+1)
            i+=1

        return nums







        # nums = list(map(str,nums))
        # awardList = []
        # i = 0
        # while i<3:
        #     tmpmax = max(nums)
        #     maxi = nums.index(tmpmax)
        #     awardList.append(maxi)
        #     nums[maxi]  = "0"
        #     i+=1
        # awarder = awarderer()
        # for i,w in zip(awardList,awarder):
        #     nums[i] = w

        # return nums

if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    test = Solution()
    r = test.findRelativeRanks(nums)
    print(r)


执行用时为 68 ms 的范例
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        newnums = sorted(list(nums),reverse=True)
        dic = {}
        l = len(newnums)
        dic[newnums[0]] = "Gold Medal"
        if l>1:
            dic[newnums[1]] = "Silver Medal"
        if l>2:
            dic[newnums[2]] = "Bronze Medal"      
        for i in range(3,len(newnums)):
            dic[newnums[i]] = str(i+1)
        res = [dic[k] for k in nums]
        return res