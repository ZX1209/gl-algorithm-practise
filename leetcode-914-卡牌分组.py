# leetcode-914-卡牌分组.py
# 用户通过次数 95
# 用户尝试次数 136
# 通过次数 97
# 提交次数 351
# 题目难度 Easy
# 给定一副牌，每张牌上都写着一个整数。

# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。

 

# 示例 1：

# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 示例 2：

# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 示例 3：

# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 示例 4：

# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 示例 5：

# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]

# 提示：

# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000

"""
思路:
先行判断..


根本没有先想好思路呢...
"""
from math import gcd

def is_primer(n):
    i = 2
    if n>6 and n % 6 != 1 and n % 6 != 5:
        return 0

    while i <= n**(1/2):
        if n%i == 0 :
            return 0
        i += 1

    return 1

def primers(n):
    for i in range(2,n+1):
        if is_primer(i):
            yield i
def f(n):
    for i in range(2,n//2+1):
        if n%i==0:
            yield i

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic = {}
        for d in deck:
            if d in dic:
                dic[d]+=1
            else:
                dic[d] = 1

        nums = list(dic.values())
        nums.sort()
        minn = nums[0]

        for p in f(minn):
            for num in nums:
                if num%p:
                    break
            return True

        return False




if __name__ == '__main__':
    deck = [1,2,3,4,4,3,2,1]
    test = Solution()
    r = test.hasGroupsSizeX(deck)
    print(r)