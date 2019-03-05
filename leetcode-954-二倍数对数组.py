# leetcode-954-二倍数对数组.py
# 用户通过次数 22
# 用户尝试次数 59
# 通过次数 22
# 提交次数 117
# 题目难度 Medium
# 给定一个长度为偶数的整数数组 A，只有对 A 进行重组后可以满足 “对于每个 0 <= i < len(A) / 2，都有 A[2 * i + 1] = 2 * A[2 * i]” 时，返回 true；否则，返回 false。

 

# 示例 1：

# 输入：[3,1,3,6]
# 输出：false
# 示例 2：

# 输入：[2,1,2,6]
# 输出：false
# 示例 3：

# 输入：[4,-2,2,-4]
# 输出：true
# 解释：我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
# 示例 4：

# 输入：[1,2,4,16,8,4]
# 输出：false
 

# 提示：

# 0 <= A.length <= 30000
# A.length 为偶数
# -100000 <= A[i] <= 100000

"""
思路:
深搜?
"""

class Solution:
    def canReorderDoubled(self, Afull):
        """
        :type A: List[int]
        :rtype: bool
        """
        Az = []
        Af = []

        for a in Afull:
            if a>=0:
                Az.append(a)
            else:
                Af.append(a)

        Az.sort()
        Af.sort(reverse = True)


        # def dfs(A):
        #     if A==[]:
        #         return True

        #     for fi,fv in enumerate(A):
        #         try:
        #             si = A.index(2*fv,fi+1)
        #             sv = A[si]

        #             A.pop(si)
        #             A.pop(fi)

        #             if dfs(A):
        #                 return True

        #             A.insert(fi,fv)
        #             A.insert(si,sv)

        #         except:
        #             return False
                        
        #     return False

        return dfs(Az) and dfs(Af)

if __name__ == '__main__':
    A = [3,1,3,6]
    test = Solution()
    r = test.canReorderDoubled(A)
    print(r)