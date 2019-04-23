# leetcode-41-缺失的第一个正数.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

# 示例 1:

# 输入: [1,2,0]
# 输出: 3
# 示例 2:

# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:

# 输入: [7,8,9,11,12]
# 输出: 1

"""
思路:
没有出现的 最小的 正整数

负数,舍弃..

连
"""

class Solution:
    def firstMissingPositive(self, nums) -> int:

        q = [0]

        for n in nums:
            if n>0:
                q.append(n)
        # print(q)
        q.sort()
        for i in range(1,len(q)):
            if q[i] - q[i-1] > 1:
                return q[i-1]+1
        return q[-1]+1

# 执行用时为 44 ms 的范例
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #第一个循环去遍历Nums里的每一个元素
        for i in range(len(nums)):
            #如果当前这个数字在我们能够进行转移的范围内
            if 0 < nums[i] and nums[i]< len(nums):
                # if nums[i] != nums[nums[i]-1]:
                #如果当前这个位置上的数字与它的index对应不上的话，我们会把它放到他应该在的正确的位置上去
                #同时为了保证数组元素信息不丢失，那个正确位置上的信息我们也要拿过来。
                while nums[i] != i + 1:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i] - 1]
                    #一旦换完后当前位置i上的元素出现以下任意一种情况都说明我们不用再换了
                    if nums[i] <= 0 or nums[i] >= len(nums) or nums[i]==nums[nums[i]-1]:
                        break
     
        #上一段代码在干的事情就是我们让大于0小于len(nums)的元素全部到对应的位置上去
        #比如nums为[1,3,-1,5,2],那么经过上面之后就变成[1,2,3,-1,5],能够对应上的数字全部已经正确排序，缺陷的(-1)的index+1就是缺失的第一个正数。
        
        jet = 1
        
        #再次遍历数组
        #jet是一个标识符，用来标志我们找没找到不符合的项
        for i in range(len(nums)):
            #找到的第一个大小与index不符的项，我们的答案就已经产生，就是当前index+1
            if nums[i] != i + 1:
                jet = 0
                ans = i + 1
                break
        #如果数组是[1,2,3]这种，每一项都符合，则缺失的是4,也就是len(nums) + 1
        if jet == 1:
            ans = len(nums)+1
        return ans

if __name__ == '__main__':
    nums = [2,1]
    test = Solution()
    r = test.firstMissingPositive(nums)
    print(r)